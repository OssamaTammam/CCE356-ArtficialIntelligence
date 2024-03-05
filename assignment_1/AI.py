from collections import deque
from BoardState import BoardState
import heapq


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

    def DFS(self) -> list[BoardState]:
        stack: list[BoardState] = []
        visited: set[BoardState] = set()

        # only use copies in a tuple storing the path it took with it
        stack.append((self.boardState, [self.boardState]))
        while stack:
            currState, currPath = stack.pop()

            if currState.checkSolved():
                self.boardState = currState
                return currPath

            visited.add(currState)
            for neighborState in currState.getNeighbors():
                if neighborState not in visited and neighborState not in stack:
                    neighbor = (neighborState, currPath + [neighborState])
                    stack.append(neighbor)

    # false -> euclidean , true -> manhattan
    def AStar(self, choice=False) -> list[BoardState]:
        heap = []
        visited: set[BoardState] = set()

        # only use copies in a tuple storing the path it took with it
        if choice:
            self.boardState.manhattanDistance()
        else:
            self.boardState.euclideanDistance()

        heapq.heappush(heap, (self.boardState, [self.boardState]))
        while heap:
            currState, currPath = heapq.heappop(heap)

            if currState.checkSolved():
                self.boardState = currState
                return currPath

            visited.add(currState)
            for neighborState in currState.getNeighbors():
                if neighborState not in visited and neighborState not in heap:
                    if choice:
                        neighborState.manhattanDistance()
                    else:
                        neighborState.euclideanDistance()

                    neighbor = (
                        neighborState,
                        currPath + [neighborState],
                    )
                    heapq.heappush(heap, neighbor)
