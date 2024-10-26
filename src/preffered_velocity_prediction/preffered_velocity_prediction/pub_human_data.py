#!/usr/bin/env python
import rclpy
from rclpy.node import Node
import numpy as np
import random
from std_msgs.msg import Float32MultiArray

class ArrayPublisher(Node):

    def __init__(self):
        super().__init__('humand_data_publisher')
        self.data_publisher = self.create_publisher(Float32MultiArray, 'lidar_readings', 10)
        self.timer = self.create_timer(0.5, self.publish_human_data)

    def publish_human_data(self):
        num_of_people = random.randint(5,10)
        buffer_data = np.random.uniform(0,2,(10,num_of_people)).astype(float)

        #array for human data
        human_data = buffer_data.flatten().tolist()

        msg = Float32MultiArray()
        msg.data = human_data

        self.get_logger().info('Publishing human data')
        self.data_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    array_publisher = ArrayPublisher()
    rclpy.spin(array_publisher)
    array_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()