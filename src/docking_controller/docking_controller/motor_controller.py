#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist

class FloatArraySubscriber(Node):
    def __init__(self):
        super().__init__('sonic_array_subscriber')
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'sonic_data',
            self.sonic_sensor_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        self.motor_pub = self.create_publisher(Twist, 'cmd_vel', 10)

        # PD controller parameters
        self.kp = 0.05
        self.kd = 0.02

        # error 
        self.error          = 0.0
        self.previous_error = 0.0

        # sensor values
        self.Front_middle   = 1
        self.Front_left     = 0
        self.Front_right    = 2
        self.Back_middle    = 4
        self.Back_left      = 3
        self.Back_right     = 5


    def sonic_sensor_callback(self, msg):
        if len(msg.data) == 6:
            self.get_logger().info(f'Received 6 floats: {msg.data}')
        else:
            self.get_logger().warn(f'Received {len(msg.data)} floats, expected 6')

        liner_velocity, angular_velocity = self.motor_controller_pid(msg.data)

        self.publish_motor_cmd (liner_velocity,angular_velocity)

    def motor_controller_pid(self, msg):
        # Implement motor control logic here
        # sensors (sensor_1: front middle, sensor_2: front left, sensor_3: front right, sensor_4: back middle, sensor_5: back left, sensor_6: back right)

        # take the back middle sensor reading as the reference
        # the difference the back middle and back left/right sensors used to calculate the error
        # if back right is the lowerst need hard turn anti clockwise
        # if back left is the lowerst need hard turn clockwise
        # if back middle is the lowerst and back left is smaller than back right means robot need to turn clockwise (soft turn)
        # if back middle is the lowerst and back right is smaller than back left means robot need to turn anti clockwise (soft turn)
        
        # motor controller = [liner velocity, angular velocity]

        linear_velocity  = 0.0  # Default forward velocity
        angular_velocity = 0.0  # Default no rotation
        
        try:
            back_middle     = msg[self.Back_middle]
            back_left       = msg[self.Back_left]
            back_right      = msg[self.Back_right]

            # find minimum sensor value
            min_sensor_value = min(back_left, back_right, back_middle)

        except:
            self.get_logger().error('Error in sensor data')
        
            linear_velocity     = 0.0
            angular_velocity    = 0.0

            return linear_velocity, angular_velocity
    

        # hard turn cases
        if back_middle <= 5.0 or back_left <= 5.0 or back_right <= 5.0:
            # stop
            linear_velocity  = 0.18
            angular_velocity = 0.0

        elif min_sensor_value == back_right:
            # Hard right turn (anti-clockwise)
            angular_velocity = 0.6

        elif min_sensor_value == back_left:
            # Hard left turn (clockwise)
            angular_velocity= -0.6

        else:
            # Soft turn case (back_mid is lowest)
            error = back_right - back_left
            angular_velocity = self.calculate_pd(error)
        
        return linear_velocity, angular_velocity
    
    def calculate_pd(self, error):
        linear_velocity  = 0.13
        derivative = error - self.previous_error

        # Calculate the control output using PD control
        control_output = (self.kp * error) + (self.kd * derivative)

        # Update the previous error
        self.previous_error = error

        control_output = max(-1.0, min(control_output, 1.0))

        return control_output
    
    def publish_motor_cmd(self,linear_velocity,angular_velocity):
        cmd = Twist()
        cmd.linear.x    = linear_velocity
        cmd.linear.y    = 0.0
        cmd.linear.z    = 0.0
        cmd.angular.x   = 0.0
        cmd.angular.y   = 0.0
        cmd.angular.z   = angular_velocity

        self.motor_pub.publish(cmd)
        self.get_logger().info(f'Command: linear={linear_velocity:.2f}, angular={angular_velocity:.2f}')
  

def main(args=None):
    rclpy.init(args=args)
    float_array_subscriber = FloatArraySubscriber()
    rclpy.spin(float_array_subscriber)
    float_array_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
