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

        # storage for previous data
        self.prev_x = {}
        self.prev_y = {}

        # update rate
        self.update_rate = 0.5 # 2 Hz

def callback_velocity_input(self, msg):
    x_positions  = msg.x #list of x positions
    y_positions = msg.y #list of y positions
    class_ids = msg.classes
    agent_count = msg.count

    # calculate velocity and update previous positions
    x_vel = []
    y_vel = []
    class_list = []

    for i, (x_position, y_position, class_id) in enumerate(zip(((x_positions), (y_positions), (class_ids)))):
        pre_x = self.prev_x.get(i, x_position)
        pre_y = self.prev_y.get(i, y_position)

        # if agent left
        if pre_x == 0 or pre_y == 0:
            vx = -1
            vy = -1
            cl_id = -1
            # remove agent from previous positions
            self.prev_x.pop(i, None)
            self.prev_y.pop(i, None)

        else:
            vx = (x_position - pre_x) / self.update_rate
            vy = (y_position - pre_y) / self.update_rate
            cl_id = class_id

        # update previous positions
        self.prev_x[i] = x_position
        self.prev_y[i] = y_position

        x_vel.append(vx)
        y_vel.append(vy)
        class_list.append(cl_id)

    # publish the velocity data
    self.publish_velocity(x_vel, y_vel, class_list)

def publish_velocity(self, x_vel,y_vel, class_list):
    pass
        

        