#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, Int32MultiArray
from smrr_interfaces.msg import Entities
import numpy as np

class VelocityExtractor(Node):
    def __init__(self):
        super().__init__('velocity_extractor')

        # subscribe to x position, y position, and class topics
        self.susbscription = self.create_subscription(
            Entities,
            '/object_tracker/laser_data_array',
            self.callback_velocity_input,
            10
            )
        
        # publisher for velocity data
        self.pub_x_velocity = self.create_publisher(Float32MultiArray, 'x_velocity', 10)
        self.pub_y_velocity = self.create_publisher(Float32MultiArray, 'y_velocity', 10)
        self.pub_class = self.create_publisher(Int32MultiArray, 'human_classes', 10)

        # storage fro previous data
        self.prev_x = {}
        self.prev_y = {}

        # update rate
        self.update_rate = 0.5 # 2 Hz

    def callback_velocity_input(self, msg):
        x_posintion  = msg.x #list of x positions
        y_position = msg.y #list of y positions
        class_id = msg.classes
        agent_count = msg.count

        # calculate velocity and update previous positions
        x_vel = []
        y_vel = []
        class_list = []

        