#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class FloatArraySubscriber(Node):
    def __init__(self):
        super().__init__('sensor_array_subscriber')
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'sensor_array_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        if len(msg.data) == 6:
            self.get_logger().info(f'Received 6 floats: {msg.data}')
        else:
            self.get_logger().warn(f'Received {len(msg.data)} floats, expected 6')

def main(args=None):
    rclpy.init(args=args)
    float_array_subscriber = FloatArraySubscriber()
    rclpy.spin(float_array_subscriber)
    float_array_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()