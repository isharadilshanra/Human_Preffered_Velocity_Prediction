DataBufferNode: Agent Data Buffer Management
Overview

The DataBufferNode is a ROS 2 node designed to manage the recent velocity and class data of dynamically changing agents (e.g., humans). Each agent is tracked with a unique ID and has a buffer that stores their last 10 entries of x and y velocities as well as class information. The node is optimized for scalability and memory efficiency, using a combination of numpy arrays and deques to handle large numbers of agents with minimal overhead.
Approach and Architecture
Goals

    Efficient Data Storage: Maintain a history of the last 10 entries for each agent.
    Dynamic Agent Handling: Add and remove agents as they enter or leave the tracking area.
    Scalable: Use memory-efficient structures to handle a large number of agents.
    ID Management: Assign a unique, incremental ID to each agent and reset IDs when reaching a threshold to prevent overflow.

Key Components

    Agent Buffer (self.agent_matrix):
        A numpy array where each row represents an agent.
        The structure of each row:
            human_id: A unique integer ID for the agent, assigned sequentially.
            x_velocities: A deque that stores the last 10 x-velocity readings.
            y_velocities: A deque that stores the last 10 y-velocity readings.
            class_ids: A deque that stores the last 10 class IDs for the agent.
        Benefit: numpy arrays allow for fast, memory-efficient operations on agent data, while deques provide automatic removal of the oldest data once the buffer reaches 10 entries.

    ID Management (next_available_id and reset_ids):
        A counter (next_available_id) provides each new agent with a unique ID.
        Reset Threshold: When next_available_id exceeds a preset threshold (e.g., 1000), all IDs are reset to keep them manageable.
        Reset Mechanism: The reset_ids function iterates over self.agent_matrix and reassigns IDs from 0 up to the current number of agents, keeping the IDs compact.

    Dynamic Agent Entry and Exit:
        Agent Entry: When new agents appear, the node adds a new row in self.agent_matrix with a unique ID and initialized data lists.
        Agent Exit: If an agent has x and y velocities set to -1, this signals that they have left the tracking area. The node removes the corresponding row, and all rows below shift up, keeping the matrix consistent with incoming data.

Workflow

    Initialization:
        self.agent_matrix is initialized as an empty numpy array with dtype=object to accommodate mixed data types (int for IDs and deque for velocities and class details).
        next_available_id starts from 0 to assign IDs to new agents.

    Data Handling (callback_velocity_data) :
        For each message from velocity_class_data, the node processes the x and y velocities and class IDs for each agent:
            New Agent: If the agent doesn’t exist in self.agent_matrix, they are added with add_new_agent.
            Existing Agent: If the agent already exists, their buffer is updated using update_existing_agent.
            Agent Exit: If both velocities are -1, the agent is removed using remove_agent.
        Logs each update to monitor the buffer’s status and ensure correct agent tracking.

    Buffer Reset:
        When next_available_id exceeds 1000, reset_ids reassigns IDs starting from 0, ensuring IDs remain low and compact without removing any data.
