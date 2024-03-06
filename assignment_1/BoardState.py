import random
from math import sqrt


class BoardState:
    def __init__(self, layout: list[int] = None) -> None:
        self.neighbors: list[BoardState] = []
        self.cost = 0

        # check if layout is present
        if layout is not None:
            self.layout = layout
        else:
            self.layout = list(range(9))
            random.shuffle(self.layout)

        self.initialLayout: list[int] = list(self.layout)

    def __lt__(self, other) -> bool:
        return self.cost <= other.cost

    def __eq__(self, other) -> bool:
        if not isinstance(other, BoardState):
            return False
        return self.layout == other.layout

    def __hash__(self) -> int:
        return hash(tuple(self.layout))

    def calcNeighbors(self) -> None:
        possibleMoves = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]  # (row, col)

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

    def getNeighbors(self) -> list["BoardState"]:
        if len(self.neighbors) == 0:
            self.calcNeighbors()

        return self.neighbors
