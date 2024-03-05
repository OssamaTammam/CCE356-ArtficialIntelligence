from BoardState import BoardState
from AI import AI


class Board:
    def __init__(self) -> None:
        self.state = BoardState()
        self.ai = AI(self.state)

    def printState(self) -> None:
        for i in range(3):
            for j in range(3):
                if j == 2:
                    print(self.state.layout[i * 3 + j])
                else:
                    print(self.state.layout[i * 3 + j], end=",")

    def BFS(self):
        return self.ai.BFS()

    def DFS(self):
        return self.ai.DFS()

    def AStar(self):
        return self.ai.AStar()

    def printPath(path):
        for state in path:
            for i in range(3):
                for j in range(3):
                    if j == 2:
                        print(state.layout[i * 3 + j])
                    else:
                        print(state.layout[i * 3 + j], end=",")
            print("")
