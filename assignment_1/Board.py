from BoardState import BoardState
from AI import AI


class Board:
    def __init__(self, layout=None) -> None:
        if layout is not None:
            self.state = BoardState(layout=layout)
        else:
            self.state = BoardState()
        self.ai = AI(self.state)

    def solve(self):
        self.ai.solve()

    def printState(self) -> None:
        print("Current board state:")
        for i in range(3):
            for j in range(3):
                if j == 2:
                    print(self.state.layout[i * 3 + j])
                else:
                    print(self.state.layout[i * 3 + j], end=",")
        print("------")

    def printAiPaths(self):
        print("BFS:")
        Board.printPath(self.ai.bfsPath)

        print("DFS:")
        Board.printPath(self.ai.dfsPath)

        print("AStar Manhattan:")
        Board.printPath(self.ai.manhattanPath)

        print("AStar Euclidean:")
        Board.printPath(self.ai.euclideanPath)

    def printPath(path):
        print(f"Number of steps taken {len(path) - 1}")
        for state in path:
            for i in range(3):
                for j in range(3):
                    if j == 2:
                        print(state.layout[i * 3 + j])
                    else:
                        print(state.layout[i * 3 + j], end=",")
            print("------")

    def reset(self):
        self.state.resetBoard()
