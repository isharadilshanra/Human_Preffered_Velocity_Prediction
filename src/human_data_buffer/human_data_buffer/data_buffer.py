#!/usr/bin/env python3

import rclpy
import numpy as np
from collections import deque
from rclpy.node import Node
from smrr_interfaces.msg import VelocityClassData

class DataBufferNode(Node):
    def __init__(self):
        super().__init__('data_buffer_node')

        # Subscribe to the velocity_class_data topic
        self.subscription = self.create_subscription(
            VelocityClassData,
            'velocity_class_data',
            self.callback_velocity_data,
            10
        )

        # Matrix to store each human's data in rows
        # Structure of each row: [human_id, x_velocities (list), y_velocities (list), class_details (list)]
        self.agent_matrix = []
        self.next_available_id = 0  # Tracks the next unique ID to assign to a new agent

    def callback_velocity_data(self, msg):
        x_velocities = msg.x_velocities  # List of x velocities from the message
        y_velocities = msg.y_velocities  # List of y velocities from the message
        class_ids = msg.class_ids        # List of class IDs from the message

        for i, (x_vel, y_vel, class_id) in enumerate(zip(x_velocities, y_velocities, class_ids)):
            
            if x_vel == -1.0 or y_vel == -1.0:
                # If the agent has left, remove their row and shift rows up
                self.remove_agent(i)
                continue

            # Update data for existing agent or add new agent
            if i < len(self.agent_matrix):
                # Existing agent - update their data
                self.agent_matrix[i][1].append(x_vel)  # Append x velocity
                self.agent_matrix[i][2].append(y_vel)  # Append y velocity
                self.agent_matrix[i][3].append(class_id)  # Append class id
            else:
                # New agent - add a new row for this agent
                self.add_new_agent(x_vel, y_vel, class_id)

            # Log buffer status for debugging
            self.log_buffer_status()

    def add_new_agent(self, x_vel, y_vel, class_id):
        # Initialize lists with a max of 10 entries each for velocities and class details
        new_row = [
            self.next_available_id,      # Assign the next available ID
            [x_vel],                     # x velocity list
            [y_vel],                     # y velocity list
            [class_id]                   # class detail list
        ]
        self.agent_matrix.append(new_row)
        self.next_available_id += 1  # Increment ID for the next new agent

    def remove_agent(self, index):
        # Remove the agent's row by index
        if index < len(self.agent_matrix):
            removed_id = self.agent_matrix[index][0]
            del self.agent_matrix[index]  # Delete the row
            self.get_logger().info(f'Removed agent with ID {removed_id} from buffer')

    def log_buffer_status(self):
        # Log the current status of the buffer for debugging
        for row in self.agent_matrix:
            self.get_logger().info(f'Agent ID: {row[0]}, X Velocities: {row[1]}, '
                                   f'Y Velocities: {row[2]}, Class Details: {row[3]}')

    def get_buffer_for_agent(self, agent_id):
        # Retrieve buffer data for a specific agent by ID
        for row in self.agent_matrix:
            if row[0] == agent_id:
                return row
        return None

    def get_all_buffers(self):
        # Retrieve buffer data for all agents
        return self.agent_matrix


def main(args=None):
    rclpy.init(args=args)
    data_buffer_node = DataBufferNode()
    rclpy.spin(data_buffer_node)
    data_buffer_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
