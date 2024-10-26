#!/usr/bin/env python
import rclpy
from rclpy.node import Node
import numpy as np
import random
from std_msgs.msg import Float32MultiArray, Int32MultiArray

class HumanPrefferedVelocity(Node):
    def __init__(self):
        super().__init__('human_preffered_velocity')
        self.data_reader = self.create_subscription(Float32MultiArray, 'lidar_readings', self.process_lidar_data,10)
        self.cls_reader = self.create_subscription(Int32MultiArray, 'human_clsses', self.process_cls_data,10)
        self.velocity_data = None
        self.cls_data = None
    def process_lidar_data(self, msg):
        
        self.velocity_data = np.array(msg.data).reshape(10,8)
        self.get_logger().info('Received data from lidar_readings')

        # check for valid data
        if self.velocity_data is not None:
            self.compute_preffered_velocity()
        else:
            self.get_logger().info('No data received')

    def process_cls_data(self, msg):
        self.cls_data = msg.data
        self.get_logger().info('Received data from human_classes')

        # check for valid data
        if self.cls_data is not None:
            self.compute_preffered_velocity()
        else:
            self.get_logger().info('No data received')

    def compute_preffered_velocity(self):
        self.get_logger().info('Computing preffered velocity')

def main(args=None):
    rclpy.init(args=args)
    human_preffered_velocity = HumanPrefferedVelocity()
    rclpy.spin(human_preffered_velocity)
    human_preffered_velocity.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

    