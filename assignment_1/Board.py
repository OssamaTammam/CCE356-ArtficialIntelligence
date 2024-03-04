from BoardState import BoardState


class Board:
    def __init__(self):
        self.state = BoardState()

    def printCurrentState(self):
        for i in range(3):
            for j in range(3):
                if j == 2:
                    print(self.state[i * 3 + j])
                else:
                    print(self.state[i * 3 + j], end=",")
