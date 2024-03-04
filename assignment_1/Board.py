from BoardState import BoardState


class Board:
    def __init__(self) -> None:
        self.state = BoardState()

    def printState(self) -> None:
        for i in range(3):
            for j in range(3):
                if j == 2:
                    print(self.state.layout[i * 3 + j])
                else:
                    print(self.state.layout[i * 3 + j], end=",")
