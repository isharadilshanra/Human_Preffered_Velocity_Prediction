#!/usr/bin/env python

# custom kalman filter class

import numpy as np

class KalmanFilter:
    def __init__(self, dim_x=2, dim_z=1):
        
        self.dim_x = dim_x
        self.dim_z = dim_z

        # initialize the matrices
        self.x = np.zeros((dim_x, 1))     # state vector
        self.F = np.eye(dim_x)            # state transition matrix (identity matrix)
        self.P = np.eye(dim_x) * 1000.0   # initial state covariance matrix (1000 for high uncertainty at the beginning)
        self.Q = np.eye(dim_x) * 0.1      # process noise covariance matrix (0.1 for low uncertainty so initially the filter will trust the model)
        self.R = np.eye(dim_z)            # measurement noise covariance matrix
        self.H = np.zeros((dim_z, dim_x)) # measurement function matrix

    def predict(self):
        self.x = np.dot(self.F, self.x)
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q

    def update(self, z):
        y = z - np.dot(self.H, self.x)  # mesurement residual
        S = np.dot(np.dot(self.H, self.P), self.H.T) + self.R  # residual covariance
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S)) # kalman gain

        # update state and covariance
        self.x = self.x + np.dot(K, y)
        self.P = self.P - np.dot(np.dot(K, self.H), self.P)

    # def set_measurement(self, z):
    #     self.H = np.eye(self.dim_z, self.dim_x)
    #     self.R = np.eye(self.dim_z) * z
    
    # def set_process_noise(self, q):
    #     self.Q = np.eye(self.dim_x) * q

    def set_state_transition(self, F):
        self.F = F

    def set_initial_state(self, x):
        self.x = x

    def set_measurement_matrix(self, H):
        self.H = H

    def set_process_noise_matrix(self, Q):
        self.Q = Q

    def set_measurement_noise(self, R):
        self.R = R