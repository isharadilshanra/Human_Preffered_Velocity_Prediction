#!/usr/bin/env python3

# import rclpy
# import numpy as np
# from collections import deque
# from rclpy.node import Node
# from smrr_interfaces.msg import VelocityClassData

# class DataBufferNode(Node):
#     def __init__(self):
#         super().__init__('data_buffer_node')

#         # Subscribe to the velocity_class_data topic
#         self.subscription = self.create_subscription(
#             VelocityClassData,
#             'velocity_class_data',
#             self.callback_velocity_data,
#             10
#         )

#         # Matrix to store each human's data in rows
#         # Structure of each row: [human_id, x_velocities (list), y_velocities (list), class_details (list)]
#         self.agent_matrix = []
#         self.next_available_id = 0  # Tracks the next unique ID to assign to a new agent

#     def callback_velocity_data(self, msg):
#         x_velocities = msg.x_velocities  # List of x velocities from the message
#         y_velocities = msg.y_velocities  # List of y velocities from the message
#         class_ids = msg.class_ids        # List of class IDs from the message

#         for i, (x_vel, y_vel, class_id) in enumerate(zip(x_velocities, y_velocities, class_ids)):
            
#             if x_vel == -1.0 or y_vel == -1.0:
#                 # If the agent has left, remove their row and shift rows up
#                 self.remove_agent(i)
#                 continue

#             # Update data for existing agent or add new agent
#             if i < len(self.agent_matrix):
#                 # Existing agent - update their data
#                 self.agent_matrix[i][1].append(x_vel)  # Append x velocity
#                 self.agent_matrix[i][2].append(y_vel)  # Append y velocity
#                 self.agent_matrix[i][3].append(class_id)  # Append class id
#             else:
#                 # New agent - add a new row for this agent
#                 self.add_new_agent(x_vel, y_vel, class_id)

#             # Log buffer status for debugging
#             self.log_buffer_status()

#     def add_new_agent(self, x_vel, y_vel, class_id):
#         # Initialize lists with a max of 10 entries each for velocities and class details
#         new_row = [
#             self.next_available_id,      # Assign the next available ID
#             [x_vel],                     # x velocity list
#             [y_vel],                     # y velocity list
#             [class_id]                   # class detail list
#         ]
#         self.agent_matrix.append(new_row)
#         self.next_available_id += 1  # Increment ID for the next new agent

#     def remove_agent(self, index):
#         # Remove the agent's row by index
#         if index < len(self.agent_matrix):
#             removed_id = self.agent_matrix[index][0]
#             del self.agent_matrix[index]  # Delete the row
#             self.get_logger().info(f'Removed agent with ID {removed_id} from buffer')

#     def log_buffer_status(self):
#         # Log the current status of the buffer for debugging
#         for row in self.agent_matrix:
#             self.get_logger().info(f'Agent ID: {row[0]}, X Velocities: {row[1]}, '
#                                    f'Y Velocities: {row[2]}, Class Details: {row[3]}')

#     def get_buffer_for_agent(self, agent_id):
#         # Retrieve buffer data for a specific agent by ID
#         for row in self.agent_matrix:
#             if row[0] == agent_id:
#                 return row
#         return None

#     def get_all_buffers(self):
#         # Retrieve buffer data for all agents
#         return self.agent_matrix


# def main(args=None):
#     rclpy.init(args=args)
#     data_buffer_node = DataBufferNode()
#     rclpy.spin(data_buffer_node)
#     data_buffer_node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()


# import rclpy
# from rclpy.node import Node
# from smrr_interfaces.msg import VelocityClassData
# import numpy as np
# from collections import deque

# class DataBufferNode(Node):
#     def __init__(self):
#         super().__init__('data_buffer_node')

#         # Subscribe to the velocity_class_data topic
#         self.subscription = self.create_subscription(
#             VelocityClassData,
#             'velocity_class_data',
#             self.callback_velocity_data,
#             10
#         )

#         # Initialize the buffer matrix with a numpy array
#         # Structure: each row is [human_id, x_velocities (deque), y_velocities (deque), class_details (deque)]
#         self.agent_matrix = np.empty((0, 4), dtype=object)
#         self.next_available_id = 0  # Tracks the next unique ID for new agents
#         self.reset_threshold = 1000  # Reset IDs if they exceed this value

#     def callback_velocity_data(self, msg):
#         x_velocities = msg.x_velocities  # List of x velocities from the message
#         y_velocities = msg.y_velocities  # List of y velocities from the message
#         class_ids = msg.class_ids        # List of class IDs from the message

#         # Process each agent's data from the message
#         for i, (x_vel, y_vel, class_id) in enumerate(zip(x_velocities, y_velocities, class_ids)):
#             # Check if the agent has left (indicated by -1 velocities)
#             if x_vel == -1.0 and y_vel == -1.0:
#                 # If agent has left, remove their row from the buffer
#                 self.remove_agent(i)
#                 continue

#             # Update data for existing agent or add new agent
#             if i < len(self.agent_matrix):
#                 # Existing agent - update their data
#                 self.update_existing_agent(i, x_vel, y_vel, class_id)
#             else:
#                 # New agent - add a new row for this agent
#                 self.add_new_agent(x_vel, y_vel, class_id)

#             # Log buffer status for debugging
#             self.log_buffer_status()

#     def add_new_agent(self, x_vel, y_vel, class_id):
#         # Initialize lists with a max of 10 entries each for velocities and class details
#         new_row = [
#             self.next_available_id,      # Assign the next available ID
#             deque([x_vel], maxlen=10),   # x velocities deque
#             deque([y_vel], maxlen=10),   # y velocities deque
#             deque([class_id], maxlen=10) # class details deque
#         ]
#         self.agent_matrix = np.vstack([self.agent_matrix, new_row])  # Add new row to the numpy matrix
#         self.next_available_id += 1  # Increment ID for the next new agent

#         # Check if ID threshold is reached and reset if necessary
#         if self.next_available_id > self.reset_threshold:
#             self.reset_ids()

#     def update_existing_agent(self, index, x_vel, y_vel, class_id):
#         # Append new data to existing agent's deques
#         self.agent_matrix[index, 1].append(x_vel)  # Update x velocities
#         self.agent_matrix[index, 2].append(y_vel)  # Update y velocities
#         self.agent_matrix[index, 3].append(class_id)  # Update class IDs

#     def remove_agent(self, index):
#         # Remove the row corresponding to the agent that has left
#         if index < len(self.agent_matrix):
#             removed_id = self.agent_matrix[index, 0]
#             self.agent_matrix = np.delete(self.agent_matrix, index, axis=0)
#             self.get_logger().info(f'Removed agent with ID {removed_id} from buffer')

#     def reset_ids(self):
#         # Reset all IDs to values from 0 up to the current number of agents
#         for idx in range(len(self.agent_matrix)):
#             self.agent_matrix[idx, 0] = idx  # Assign IDs starting from 0
#         self.next_available_id = len(self.agent_matrix)  # Set the next ID after the last used ID
#         self.get_logger().info("Reset all human IDs in the buffer.")

#     def log_buffer_status(self):
#         # Log the current status of the buffer for debugging
#         for row in self.agent_matrix:
#             self.get_logger().info(f'Agent ID: {row[0]}, X Velocities: {list(row[1])}, '
#                                    f'Y Velocities: {list(row[2])}, Class Details: {list(row[3])}')

#     def get_buffer_for_agent(self, agent_id):
#         # Retrieve buffer data for a specific agent by ID
#         agent_row = self.agent_matrix[self.agent_matrix[:, 0] == agent_id]
#         return agent_row if agent_row.size else None

#     def get_all_buffers(self):
#         # Retrieve buffer data for all agents
#         return self.agent_matrix


# def main(args=None):
#     rclpy.init(args=args)
#     data_buffer_node = DataBufferNode()
#     rclpy.spin(data_buffer_node)
#     data_buffer_node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()


# buffer with statistics for each agent in the multy dimetional numpy array

import rclpy
from rclpy.node import Node
from smrr_interfaces.msg import VelocityClassData
import numpy as np
from collections import deque, Counter

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

        # Initialize the buffer matrix with a numpy array
        # Structure: each row is [human_id, x_velocities (deque), y_velocities (deque), class_details (deque), statistics (dict)]
        self.agent_matrix = np.empty((0, 5), dtype=object)
        self.next_available_id = 0  # Tracks the next unique ID for new agents
        self.reset_threshold = 1000  # Reset IDs if they exceed this value

    def callback_velocity_data(self, msg):
        x_velocities = msg.x_velocities  # List of x velocities from the message
        y_velocities = msg.y_velocities  # List of y velocities from the message
        class_ids = msg.class_ids        # List of class IDs from the message

        try:
            # Process each agent's data from the message
            for i, (x_vel, y_vel, class_id) in enumerate(zip(x_velocities, y_velocities, class_ids)):
                # Check if the agent has left (indicated by -1 velocities)

                if x_vel == -1.0 and y_vel == -1.0:
                    # If agent has left, remove their row from the buffer
                    try:
                        self.remove_agent(i)
                    except Exception as e:
                        self.get_logger().error(f"Error removing agent from buffer: {e}")
                    continue

                # Update data for existing agent or add new agent
                if i < len(self.agent_matrix):
                    # Existing agent - update their data
                    try:
                        self.update_existing_agent(i, x_vel, y_vel, class_id)
                    except Exception as e:
                        self.get_logger().error(f"Error updating existing agent in buffer: {e}")
                else:
                    # New agent - add a new row for this agent
                    try:
                        self.add_new_agent(x_vel, y_vel, class_id)

                    except Exception as e:
                        self.get_logger().error(f"Error adding new agent to buffer: {e}")

                # Calculate and store statistics after updating each agent
                try:
                    self.calculate_statistics(i)
                except Exception as e:
                    self.get_logger().error(f"Error calculating statistics for agent in buffer: {e}")

                
                # Log buffer status for debugging
                try:
                    self.log_buffer_status()
                except Exception as e:
                    self.get_logger().error(f"Error logging buffer status in the loop: {e}")

        except Exception as e:
            self.get_logger().error(f"Error assigning data to buffer in the loop: {e}")

    def add_new_agent(self, x_vel, y_vel, class_id):
        # Initialize lists with a max of 10 entries each for velocities and class details, plus a dictionary for statistics
        new_row = [
            self.next_available_id,      # Assign the next available ID
            deque([x_vel], maxlen=10),   # x velocities deque
            deque([y_vel], maxlen=10),   # y velocities deque
            deque([class_id], maxlen=10), # class details deque
            {}                           # Placeholder for statistics dictionary
        ]
        self.agent_matrix = np.vstack([self.agent_matrix, new_row])  # Add new row to the numpy matrix
        self.next_available_id += 1  # Increment ID for the next new agent

        # Check if ID threshold is reached and reset if necessary
        if self.next_available_id > self.reset_threshold:
            self.reset_ids()

    def update_existing_agent(self, index, x_vel, y_vel, class_id):
        # Append new data to existing agent's deques
        self.agent_matrix[index, 1].append(x_vel)  # Update x velocities
        self.agent_matrix[index, 2].append(y_vel)  # Update y velocities
        self.agent_matrix[index, 3].append(class_id)  # Update class IDs

    def calculate_statistics(self, index):
        # Calculate statistics for the agent's velocities and class data
        x_vals = np.array(self.agent_matrix[index, 1])  # Convert x velocities to numpy array
        y_vals = np.array(self.agent_matrix[index, 2])  # Convert y velocities to numpy array
        class_vals = list(self.agent_matrix[index, 3])   # Convert class IDs to a list

        # Compute mean, standard deviation, and variance for x and y velocities
        x_mean = np.mean(x_vals)
        y_mean = np.mean(y_vals)
        x_std_dev = np.std(x_vals)
        y_std_dev = np.std(y_vals)
        x_variance = np.var(x_vals)
        y_variance = np.var(y_vals)

        # Determine the majority class ID (most common value)
        majority_class_id = Counter(class_vals).most_common(1)[0][0]

        # Store the calculated statistics in the agent's statistics dictionary
        self.agent_matrix[index, 4] = {
            "x_mean": x_mean,
            "y_mean": y_mean,
            "x_std_dev": x_std_dev,
            "y_std_dev": y_std_dev,
            "x_variance": x_variance,
            "y_variance": y_variance,
            "majority_class_id": majority_class_id
        }

    def remove_agent(self, index):
        # Remove the row corresponding to the agent that has left
        if index < len(self.agent_matrix):
            removed_id = self.agent_matrix[index, 0]
            self.agent_matrix = np.delete(self.agent_matrix, index, axis=0)
            self.get_logger().info(f'Removed agent with ID {removed_id} from buffer')

    def reset_ids(self):
        # Reset all IDs to values from 0 up to the current number of agents
        for idx in range(len(self.agent_matrix)):
            self.agent_matrix[idx, 0] = idx  # Assign IDs starting from 0
        self.next_available_id = len(self.agent_matrix)  # Set the next ID after the last used ID
        self.get_logger().info("Reset all human IDs in the buffer.")

    def log_buffer_status(self):
        # Log the current status of the buffer for debugging
        for row in self.agent_matrix:
            stats = row[4] if row[4] else {}  # Access the statistics column
            self.get_logger().info(f'Agent ID: {row[0]}, X Velocities: {list(row[1])}, '
                                   f'Y Velocities: {list(row[2])}, Class Details: {list(row[3])}, '
                                   f'Statistics: {stats}')

    def get_buffer_for_agent(self, agent_id):
        # Retrieve buffer data for a specific agent by ID
        agent_row = self.agent_matrix[self.agent_matrix[:, 0] == agent_id]
        return agent_row if agent_row.size else None

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


