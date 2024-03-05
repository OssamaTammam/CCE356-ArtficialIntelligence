from collections import deque
from BoardState import BoardState


class AI:
    # goal = BoardState.goal

    def __init__(self, boardState):
        self.boardState: BoardState = boardState

    def BFS(self) -> list[BoardState]:
        queue: deque[BoardState] = deque()
        visited: set[BoardState] = set()

        # only use copies in a tuple storing the path it took with it
        queue.append((self.boardState, [self.boardState]))
        while queue:
            currState, currPath = queue.popleft()

            if currState.checkSolved():
                self.boardState = currState
                return currPath

            visited.add(currState)
            for neighborState in currState.getNeighbors():
                if neighborState not in visited:
                    neighbor = (neighborState, currPath + [neighborState])
                    queue.append(neighbor)
