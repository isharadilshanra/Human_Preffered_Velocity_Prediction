#!/usr/bin/env python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, Int32MultiArray
from collections import defaultdict, deque
from smrr_interfaces.msg import Entities

class AgentBuffer:
    def __init__(self):
        # Dictionary to hold each agent's velocity and class data
        # The structure is {agent_id: {"x": deque, "y": deque, "class_id": int}}
        self.buffer = defaultdict(lambda: {"x": deque(maxlen=10), "y": deque(maxlen=10), "class_id": None})

    def update_agent(self, agent_id, x_velocity, y_velocity, class_id):
        # Update the deque buffer for x and y velocities
        self.buffer[agent_id]["x"].append(x_velocity)
        self.buffer[agent_id]["y"].append(y_velocity)
        # Update the class id (latest value)
        self.buffer[agent_id]["class_id"] = class_id

    def cleanup_agents(self):
        # Remove agents that have exited (when both x and y velocities are zero)
        to_remove = [agent_id for agent_id, data in self.buffer.items()
                     if all(v == 0 for v in data["x"]) and all(v == 0 for v in data["y"])]
        for agent_id in to_remove:
            del self.buffer[agent_id]

    def get_agent_data(self, agent_id):
        # Returns the buffered data for a specific agent
        return self.buffer.get(agent_id, None)

    def get_all_agents_data(self):
        # Returns all buffered data
        return self.buffer


class BufferNode(Node):
    def __init__(self):
        super().__init__('velocity_buffer_node')
        
        # Initialize AgentBuffer to hold agent data
        self.agent_buffer = AgentBuffer()

        # Subscribers for x velocity, y velocity, and class topics
        self.sub_x_velocity = self.create_subscription(Float32MultiArray, 'x_velocity', self.callback_x_velocity, 10)
        self.sub_y_velocity = self.create_subscription(Float32MultiArray, 'y_velocity', self.callback_y_velocity, 10)
        self.sub_class = self.create_subscription(Int32MultiArray, 'human_classes', self.callback_class, 10)

        # Temporary storage for each update, flushed every cycle
        self.latest_x_velocity = []
        self.latest_y_velocity = []
        self.latest_classes = []

    def callback_x_velocity(self, msg):
        self.latest_x_velocity = msg.data
        self.update_buffer_if_complete()

    def callback_y_velocity(self, msg):
        self.latest_y_velocity = msg.data
        self.update_buffer_if_complete()

    def callback_class(self, msg):
        self.latest_classes = msg.data
        self.update_buffer_if_complete()

    def update_buffer_if_complete(self):
        # Check if all three lists are populated
        if self.latest_x_velocity and self.latest_y_velocity and self.latest_classes:
            # Loop through each human and update the buffer
            for i, (x_vel, y_vel, class_id) in enumerate(zip(self.latest_x_velocity, self.latest_y_velocity, self.latest_classes)):
                self.agent_buffer.update_agent(i, x_vel, y_vel, class_id)

            # Perform cleanup to remove exited agents
            self.agent_buffer.cleanup_agents()

            # Log current buffer status (optional for debugging)
            self.get_logger().info(f'Updated agent buffer: {self.agent_buffer.get_all_agents_data()}')

            # Clear the temporary data holders for the next update cycle
            self.latest_x_velocity = []
            self.latest_y_velocity = []
            self.latest_classes = []


def main(args=None):
    rclpy.init(args=args)
    buffer_node = BufferNode()
    rclpy.spin(buffer_node)
    buffer_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
