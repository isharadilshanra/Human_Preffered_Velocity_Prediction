#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import random
import time

class FloatArrayPublisher(Node):
    def __init__(self):
        super().__init__('sensor_array_publisher')
        # [sensor_1, sensor_2, sensor_3, sensor_4, sensor_5, sensor_6]

        self.publisher_ = self.create_publisher(Float32MultiArray, 'sensor_array_topic', 10)
        timer_period = 0.05  # 50ms (20Hz)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        #self.i = 0

    def timer_callback(self):
        msg = Float32MultiArray()
        msg.data = [random.random() * 100 for _ in range(6)]  # Generate 6 random floats
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        #self.i += 1

def main(args=None):
    rclpy.init(args=args)
    float_array_publisher = FloatArrayPublisher()
    rclpy.spin(float_array_publisher)
    float_array_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()