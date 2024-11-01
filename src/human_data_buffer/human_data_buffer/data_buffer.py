#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from collections import defaultdict, deque
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

        # Buffer dictionary where each agent has a fixed-size buffer for x, y velocities and class data
        # Structure: {agent_id: {"x": deque, "y": deque, "class_id": deque}}
        self.agent_buffers = defaultdict(lambda: {
            "x": deque(maxlen=10),
            "y": deque(maxlen=10),
            "class_id": deque(maxlen=10)
        })

    def callback_velocity_data(self, msg):
        x_velocities = msg.x_velocities  # List of x velocities
        y_velocities = msg.y_velocities  # List of y velocities
        class_ids = msg.class_ids        # List of class IDs

        # Process each agent's data from the message
        for i, (x_vel, y_vel, class_id) in enumerate(zip(x_velocities, y_velocities, class_ids)):
            # If x and y velocities are -1, the agent has left; remove them from the buffer
            if x_vel == -1.0 and y_vel == -1.0:
                if i in self.agent_buffers:
                    del self.agent_buffers[i]
                    self.get_logger().info(f'Removed agent {i} from buffer')
                continue

            # Add the new data to the buffer for each agent
            self.agent_buffers[i]["x"].append(x_vel)
            self.agent_buffers[i]["y"].append(y_vel)
            self.agent_buffers[i]["class_id"].append(class_id)

            # Log buffer status for debugging
            self.get_logger().info(f'Updated buffer for agent {i}: '
                                   f'X Velocities: {list(self.agent_buffers[i]["x"])}, '
                                   f'Y Velocities: {list(self.agent_buffers[i]["y"])}, '
                                   f'Class IDs: {list(self.agent_buffers[i]["class_id"])}')

    def get_buffer_for_agent(self, agent_id):
        # Retrieve buffer data for a specific agent
        return self.agent_buffers.get(agent_id, None)

    def get_all_buffers(self):
        # Retrieve buffer data for all agents
        return self.agent_buffers


def main(args=None):
    rclpy.init(args=args)
    data_buffer_node = DataBufferNode()
    rclpy.spin(data_buffer_node)
    data_buffer_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
