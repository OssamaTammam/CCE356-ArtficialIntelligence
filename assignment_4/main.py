import numpy as np


class GridWorld:
    def __init__(self, r):
        self.grid = np.array([[r, -1, 10], [-1, -1, -1], [-1, -1, -1]])
        self.actions = ["Up", "Left", "Down", "Right"]  # Updated actions
        self.transition_probs = {
            "Up": [(0.8, -1, 0), (0.1, 0, -1), (0.1, 0, 1)],
            "Down": [(0.8, 1, 0), (0.1, 0, -1), (0.1, 0, 1)],
            "Right": [(0.8, 0, 1), (0.1, -1, 0), (0.1, 1, 0)],
            "Left": [(0.8, 0, -1), (0.1, -1, 0), (0.1, 1, 0)],
        }
        self.num_rows, self.num_cols = self.grid.shape
        self.discount = 0.99
        self.threshold = 1e-6

    def value_iteration(self):
        V = np.zeros_like(self.grid, dtype=float)
        for _ in range(100):
            delta = 0  # Maximum change in any state
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    if self.grid[i, j] == -1:  # Not a terminal state
                        max_v = float("-inf")
                        for action in self.transition_probs:
                            value = 0
                            for prob, di, dj in self.transition_probs[action]:
                                new_i, new_j = self._get_new_position(i, j, di, dj)
                                value += prob * V[new_i, new_j]
                            new_v = self.grid[i, j] + self.discount * value
                            max_v = max(max_v, new_v)
                            delta = max(delta, np.abs(new_v - V[i, j]))
                        V[i, j] = max_v

                    else:
                        V[i, j] = self.grid[i, j]
            if delta < self.threshold:
                break

        return V

    def extract_policy(self, V):
        policy = np.zeros_like(self.grid, dtype=str)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.grid[i, j] == -1:
                    max_v = float("-inf")
                    best_action = None
                    for action in self.transition_probs:
                        value = 0
                        for prob, di, dj in self.transition_probs[action]:
                            new_i, new_j = self._get_new_position(i, j, di, dj)
                            value += prob * V[new_i, new_j]
                        new_v = self.grid[i, j] + self.discount * value
                        if new_v > max_v:
                            max_v = new_v
                            best_action = action
                    policy[i, j] = best_action
                else:
                    policy[i, j] = "T"
        return policy

    def _get_new_position(self, i, j, di, dj):
        new_i = i + di
        new_j = j + dj
        if 0 <= new_i < self.num_rows and 0 <= new_j < self.num_cols:
            return new_i, new_j
        return i, j


def main():
    r_values = [100, 3, 0, -3]
    for r in r_values:
        print(f"Value Iteration for r={r}:")
        gridworld = GridWorld(r)
        V = gridworld.value_iteration()
        policy = gridworld.extract_policy(V)
        print("Value function:")
        print(V)
        print("Policy:")
        print(policy)


if __name__ == "__main__":
    main()
