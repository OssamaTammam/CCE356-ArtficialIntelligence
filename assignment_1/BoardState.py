import random


class BoardState:
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, layout: list = None, boardState: "BoardState" = None):
        self.neighbors = []

        # check if it's already an object and clone it
        if boardState is not None:
            self.layout = boardState.layout.copy()
            self.neighbors = boardState.neighbors.copy()
            return

        # check if layout is present
        if layout is not None:
            self.layout = layout

        # if layout is not specified generate a random layout
        if layout is None and boardState is None:
            self.layout = list(range(9))
            random.shuffle(self.layout)

    def calcNeighbors(self):
        possibleMoves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (row, col)
        zeroIndex = self.layout.index(0)
        currRow, currCol = zeroIndex // 3, zeroIndex % 3

        for rowMove, colMove in possibleMoves:
            newRow, newCol = currRow + rowMove, currCol + colMove

            if 0 <= newRow < 3 and 0 <= newCol < 3:
                neighborLayout = list(self.layout)

                newZeroIndex = newRow * 3 + newCol
                neighborLayout[zeroIndex], neighborLayout[newZeroIndex] = (
                    neighborLayout[newZeroIndex],
                    neighborLayout[zeroIndex],
                )

                neighbor = BoardState(layout=neighborLayout)
                self.neighbors.append(neighbor)

    def getNeighbors(self):
        if len(self.neighbors) == 0:
            self.calcNeighbors()

        return self.neighbors

    def checkSolved(self):
        return True if self.layout == BoardState.goal else False
