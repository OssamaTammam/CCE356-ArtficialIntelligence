import numpy as np

# Define the grid world and rewards
grid_world = np.array([[-1, 10, -1], [-1, -1, -1], [-1, -1, -1]])

# Define the discount factor
gamma = 0.99

# Define the possible actions: Up, Down, Right, Left
actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# Function to check if a state is valid
def is_valid_state(state):
    x, y = state
    return 0 <= x < grid_world.shape[0] and 0 <= y < grid_world.shape[1]


# Function to compute the value for a given state and action
def compute_value(state, action, V):
    x, y = state
    dx, dy = action

    # Compute the next state after taking action
    next_state = (x + dx, y + dy)

    # If next state is valid
    if is_valid_state(next_state):
        return grid_world[next_state] + gamma * V[next_state[0], next_state[1]]
    else:
        # If next state is invalid (hit wall), stay in the same state
        return grid_world[x, y] + gamma * V[x, y]


# Perform value iteration for each value of r
for r in [100, 3, 0, -32]:
    # Initialize the value function
    V = np.zeros_like(grid_world, dtype=float)

    # Perform value iteration until convergence
    while True:
        delta = 0
        for i in range(grid_world.shape[0]):
            for j in range(grid_world.shape[1]):
                if (i, j) != (0, 1):  # Avoid updating the terminal state
                    temp_v = V[i, j]
                    max_value = float("-inf")
                    for action in actions:
                        value = compute_value((i, j), action, V)
                        if value > max_value:
                            max_value = value
                    V[i, j] = max_value
                    delta = max(delta, abs(temp_v - V[i, j]))
        if delta < 1e-6:
            break

    # Compute the policy
    policy = np.zeros_like(grid_world, dtype=str)
    for i in range(grid_world.shape[0]):
        for j in range(grid_world.shape[1]):
            if (i, j) == (0, 1):  # Terminal state
                policy[i, j] = "T"
            else:
                max_value = float("-inf")
                best_action = None
                for action in actions:
                    value = compute_value((i, j), action, V)
                    if value > max_value:
                        max_value = value
                        best_action = action
                if best_action == (0, 1):
                    policy[i, j] = "T"
                elif best_action == (0, -1):
                    policy[i, j] = "←"
                elif best_action == (1, 0):
                    policy[i, j] = "↓"
                elif best_action == (-1, 0):
                    policy[i, j] = "↑"

    # Print the value function and policy
    print(f"Value function for r = {r}:\n{V}\n")
    print(f"Policy for r = {r}:\n{policy}\n")
