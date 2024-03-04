import random


class BoardState:
    def __init__(self, state=None):
        if state is None:
            self.state = list(range(9))
            random.shuffle(self.state)
        else:
            self.state = state
        self.goalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.neighboringStates = []
        self.calcNeighbors()

    def calcNeighbors(self):
        possibleMoves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (row, col)
        zeroIndex = self.state.index(0)
        currRow, currCol = zeroIndex // 3, zeroIndex % 3

        for rowMove, colMove in possibleMoves:
            newRow, newCol = currRow + rowMove, currCol + colMove

            if 0 <= newRow < 3 and 0 <= newCol < 3:
                neighbor = list(self.state)
                newZeroIndex = newRow * 3 + newCol
                self.state[zeroIndex], self.state[newZeroIndex] = (
                    self.state[newZeroIndex],
                    self.state[zeroIndex],
                )

                self.neighboringStates.append(neighbor)

    def getNeighboringStates(self):
        return self.neighboringStates

    def checkSolved(self):
        return True if self.state == self.goalState else False
