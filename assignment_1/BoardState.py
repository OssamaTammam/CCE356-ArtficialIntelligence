import random


class BoardState:
    goalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, state: list = None, boardState: "BoardState" = None):
        # check if it's already an object and clone it
        if boardState is not None:
            self.state = boardState.state.copy()
            self.neighbors = boardState.neighbors.copy()
            return

        # check if state is present
        if state is not None:
            self.state = state

        # if state is not specified generate a random state
        if state is None and boardState is None:
            self.state = list(range(9))
            random.shuffle(self.state)

        # calculate the neighboring states for each board
        self.neighbors = []

    def calcNeighbors(self):
        possibleMoves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (row, col)
        zeroIndex = self.state.index(0)
        currRow, currCol = zeroIndex // 3, zeroIndex % 3

        for rowMove, colMove in possibleMoves:
            newRow, newCol = currRow + rowMove, currCol + colMove

            if 0 <= newRow < 3 and 0 <= newCol < 3:
                neighborState = list(self.state)

                newZeroIndex = newRow * 3 + newCol
                neighborState[zeroIndex], neighborState[newZeroIndex] = (
                    neighborState[newZeroIndex],
                    neighborState[zeroIndex],
                )

                neighbor = BoardState(state=neighborState)
                self.neighbors.append(neighbor)

    def getNeighbors(self):
        return self.neighbors

    def checkSolved(self):
        return True if self.state == BoardState.goalState else False
