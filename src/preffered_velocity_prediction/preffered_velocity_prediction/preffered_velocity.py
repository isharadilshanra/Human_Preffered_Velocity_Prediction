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
        kf.P *= 1000.  # Initial high uncertainty of Initial Covariance Matrix
        kf.R = 1.0  # Initial measurement noise (will be updated later)
        kf.Q = np.array([[0.1, 0.0], [0.0, 0.1]])  # Process noise (will be updated later)
        return kf

    def update_filter_parameters(self, kf, class_id, std_dev, variance):
        # update the parameters of the kalman filter based on the class id
        if class_id == 0:  # Children (typically more erratic)
            base_R = 2.0  # Base measurement noise
            base_Q = 1.5  # Base process noise factor
        elif class_id == 1:  # Normal adults
            base_R = 1.0
            base_Q = 1.0
        elif class_id == 2:  # Seniors (usually smoother)
            base_R = 0.8
            base_Q = 0.8
        elif class_id == 3:  # People with disabilities
            base_R = 0.5
            base_Q = 0.5
        else:
            # Default values
            base_R = 1.0
            base_Q = 1.0

        # Adjust measurement noise R based on the variance (higher variance, higher noise)
        kf.R = base_R * (1 + variance / (1 + variance))  # Scale R using variance
        
        # Adjust process noise Q based on standard deviation (higher std_dev, more flexibility)
        kf.Q = np.array([[base_Q * (1 + std_dev), 0], [0, base_Q * (1 + std_dev)]])

 

    def update_kalman_filters(self, num_people):
        if num_people > len(self.filters):
            for i in range(num_people - len(self.filters)):
                self.filters.append(self.kalman_filter())
        
        elif num_people < len(self.filters):
            self.filters = self.filters[:num_people]

        self.num_of_people = num_people

        
    def process_lidar_data(self, msg):
        
        self.velocity_data = np.array(msg.data).reshape(-1, len(msg.data) // 3) # assumes 3 rows of statics per human
        # -1 assumes that the number of humans is unknown
        num_people = self.velocity_data.shape[1]
        self.get_logger().info('Received data from lidar_readings with {} people'.format(num_people))

        if num_people != self.num_of_people:
            # handles different number of people (people entering or leaving the scene)
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

        self.get_logger().info('Computing preffered velocity')

        # Extract mean, std deviation, and variance data from the incoming array
        mean_velocity = self.velocity_data[0, :]
        std_devs = self.velocity_data[1, :]
        variances = self.velocity_data[2, :]

        preferred_velocity = [] # list of preferred velocities for each human

        # loop through each human
        for i in range (self.num_of_people):
            mean_velocity_i = mean_velocity[i]

            # handle the case where class data is not available 
            if (len(self.cls_data) -1) < i:
                class_id = 1 # default to normal adults
            else:
                class_id = self.cls_data[i]

            kf = self.filters[i]

            # update filter parameters base on class id
            self.update_filter_parameters(kf, class_id, std_devs[i], variances[i])

            # predict the next state and update
            kf.predict()
            kf.update(np.array([[mean_velocity_i]]))

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

    