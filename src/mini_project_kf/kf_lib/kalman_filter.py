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

    