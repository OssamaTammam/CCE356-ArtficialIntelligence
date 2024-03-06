from BoardState import BoardState
from AI import AI


class Board:
    def __init__(self, layout: list[int] = None) -> None:
        if layout is not None:
            self.state: BoardState = BoardState(layout=layout)
        else:
            self.state: BoardState = BoardState()
        self.ai: AI = AI(self.state)

    def solve(self) -> None:
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

    def printAiPaths(self) -> None:
        print("BFS:")
        Board.printPath(self.ai.bfsPath)

        print("DFS:")
        Board.printPath(self.ai.dfsPath)

        print("Iterative Deepening DFS:")
        Board.printPath(self.ai.iddfsPath)

        print("AStar Manhattan:")
        Board.printPath(self.ai.manhattanPath)

        print("AStar Euclidean:")
        Board.printPath(self.ai.euclideanPath)

    def printPath(path: list[BoardState]) -> None:
        print(f"Number of steps taken {len(path) - 1}")
        for state in path:
            for i in range(3):
                for j in range(3):
                    if j == 2:
                        print(state.layout[i * 3 + j])
                    else:
                        print(state.layout[i * 3 + j], end=",")
            print("------")

    def reset(self) -> None:
        self.state.resetBoard()
