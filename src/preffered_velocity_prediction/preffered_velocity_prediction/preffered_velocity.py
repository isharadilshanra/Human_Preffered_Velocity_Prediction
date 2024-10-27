#!/usr/bin/env python
import rclpy
from rclpy.node import Node
import numpy as np
import random
from std_msgs.msg import Float32MultiArray, Int32MultiArray
from filterpy.kalman import KalmanFilter

class HumanPrefferedVelocity(Node):
    def __init__(self):
        super().__init__('human_preffered_velocity')
        self.data_reader = self.create_subscription(Float32MultiArray, 'lidar_readings', self.process_lidar_data,10)
        self.cls_reader = self.create_subscription(Int32MultiArray, 'human_clsses', self.process_cls_data,10)
        self.velocity_data = []
        self.cls_data = []

        self.filters = []
        self.num_of_people = 0
        

    def kalman_filter(self):
        # initialize kalman filter 
        # each human will have its own kalman filter
        kf = KalmanFilter(dim_x=2, dim_z=1)
        kf.x = np.array([[0.], [0.]])  # Start with zero speed and acceleration
        kf.F = np.array([[1., 1.], [0., 1.]])  # Constant velocity model
        kf.H = np.array([[1., 0.]])  # Measure speed only
        kf.P *= 1000.  # Initial uncertainty
        kf.R = 1.0  # Initial measurement noise
        kf.Q = np.array([[0.1, 0.0], [0.0, 0.1]])  # Process noise
        return kf

    def update_filter_parameters(self, kf,class_id):
        # update the parameters of the kalman filter
        # based on the class id of the human

        if class_id == 0:  # Children
            kf.R = 2.0 # Increase the measurement noise
            kf.Q *= 1.5 # Increase the process noise
        elif class_id == 1:  # Normal adults
            kf.R = 1.0
            kf.Q *= 1.0
        elif class_id == 2:  # Seniors
            kf.R = 0.8
            kf.Q *= 0.8
        elif class_id == 3:  # People with disabilities
            kf.R = 0.5
            kf.Q *= 0.5
        else:
            # Default values
            kf.R = 1.0
            kf.Q *= 1.0

    def update_kalman_filters(self, num_people):
        if num_people > len(self.filters):
            for i in range(num_people - len(self.filters)):
                self.filters.append(self.kalman_filter())
        
        elif num_people < len(self.filters):
            self.filters = self.filters[:num_people]

        self.num_of_people = num_people

        
    def process_lidar_data(self, msg):
        
        self.velocity_data = np.array(msg.data).reshape(-1, len(msg.data) // 10) # 10 assumes 10 lidar readings per human
        # -1 assumes that the number of humans is unknown
        num_people = self.velocity_data.shape[1]
        self.get_logger().info('Received data from lidar_readings with {} people'.format(num_people))

        if num_people != self.num_of_people:
            # handles different number of people
            self.update_kalman_filters(num_people)

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
        # Ensure that cls_data has the same number of entries as the number of agents
        if len(self.cls_data) != self.num_of_people:
            self.get_logger().info('Mismatch between number of agents in velocity data and class data.')
            return
        
        self.get_logger().info('Computing preffered velocity')

        mean_velocity = np.mean(self.velocity_data, axis=0)
        ##mean_velocity = mean_velocity.reshape(-1, 1)
        preferred_velocity = [] # list of preferred velocities for each human

        # loop through each human
        for i in range (self.num_of_people):
            mean_velocity_i = mean_velocity[i]
            class_id = self.cls_data[i]
            kf = self.filters[i]

            # update filter parameters base on class id
            self.update_filter_parameters(kf, class_id)

            # predict the next state and update
            kf.predict()
            kf.update(np.array([mean_velocity_i]))

            # get the preferred velocity
            preferred_velocity_i = kf.x[0, 0]
            preferred_velocity.append(preferred_velocity_i)

        self.get_logger().info(f'Agent {i} - class: {class_id}, '
                               f'Observed velocity: {mean_velocity_i:.2f}, '
                               f'Preferred velocity: {preferred_velocity_i:.2f}')
        
        # create a publisher & publish the preferred velocity

def main(args=None):
    rclpy.init(args=args)
    human_preffered_velocity = HumanPrefferedVelocity()
    rclpy.spin(human_preffered_velocity)
    human_preffered_velocity.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

    