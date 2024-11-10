#!/usr/bin/env python

# custom kalman filter class

import numpy as np

class KalmanFilter:
    def __init__(self, dim_x=2, dim_z=1):
        
        self.dim_x = dim_x
        self.dim_z = dim_z

        # initialize the matrices
        self.X = np.zeros((dim_x, 1))     # state vector
        self.F = np.eye(dim_x)            # state transition matrix (identity matrix)
        self.P = np.eye(dim_x) * 1000.0   # initial state covariance matrix (1000 for high uncertainty at the beginning)
        self.Q = np.eye(dim_x) * 0.1      # process noise covariance matrix (0.1 for low uncertainty so initially the filter will trust the model)
        self.R = np.eye(dim_z)            # measurement noise covariance matrix
        self.H = np.zeros((dim_z, dim_x)) # measurement function matrix

    def predict(self):
        # add dimention checks for runtime error handling
        assert self.X.shape == (self.dim_x, 1), f"x shape should be ({self.dim_x}, 1)"
        assert self.F.shape == (self.dim_x, self.dim_x), f"F shape should be ({self.dim_x}, {self.dim_x})"
        assert self.P.shape == (self.dim_x, self.dim_x), f"P shape should be ({self.dim_x}, {self.dim_x})"
        assert self.Q.shape == (self.dim_x, self.dim_x), f"Q shape should be ({self.dim_x}, {self.dim_x})"

        # predict the state and covariance
        self.X = self.F @ self.X # @ means matrix multiplication
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self, z):

        # add dimention checks for runtime error handling
        assert self.H.shape == (self.dim_z, self.dim_x), f"H shape should be ({self.dim_z}, {self.dim_x})"
        assert self.R.shape == (self.dim_z, self.dim_z), f"R shape should be ({self.dim_z}, {self.dim_z})"
        assert z.shape == (self.dim_z, 1), f"z shape should be ({self.dim_z}, 1)"

        y = z - np.dot(self.H, self.X)  # mesurement residual
        S = np.dot(np.dot(self.H, self.P), self.H.T) + self.R + 1e-5 # residual covariance
        K = self.P @ self.H.T @ np.linalg.inv(S)

        # update state and covariance
        self.X = self.X + np.dot(K, y)
        self.P = (np.eye(self.dim_x) - np.dot(K, self.H)) @ self.P

    # def set_measurement(self, z):
    #     self.H = np.eye(self.dim_z, self.dim_x)
    #     self.R = np.eye(self.dim_z) * z
    
    # def set_process_noise(self, q):
    #     self.Q = np.eye(self.dim_x) * q

    def set_state_transition(self, F):
        assert F.shape == (self.dim_x, self.dim_x), f"F shape should be ({self.dim_x}, {self.dim_x})"
        self.F = F

    def set_initial_state(self, x):
        assert x.shape == (self.dim_x, 1), f"x shape should be ({self.dim_x}, 1)"
        self.X = x

    def set_measurement_matrix(self, H):
        assert H.shape == (self.dim_z, self.dim_x), f"H shape should be ({self.dim_z}, {self.dim_x})"
        self.H = H

    def set_process_noise_matrix(self, Q):
        assert Q.shape == (self.dim_x, self.dim_x), f"Q shape should be ({self.dim_x}, {self.dim_x})"
        self.Q = Q

    def set_measurement_noise(self, R):
        assert R.shape == (self.dim_z, self.dim_z), f"R shape should be ({self.dim_z}, {self.dim_z})"
        self.R = R