from collections import deque
from BoardState import BoardState
import heapq
from time import time


class AI:
    def __init__(self, boardState):
        self.boardState: BoardState = boardState
        self.bfsPath = []
        self.dfsPath = []
        self.manhattanPath = []
        self.euclideanPath = []
        self.iddfsPath = []

    def solve(self):
        startTime = time()
        self.bfsPath = self.BFS()
        print(f"BFS Time: {time() - startTime}")
        startTime = time()
        self.dfsPath = self.DFS()
        print(f"DFS Time: {time() - startTime}")
        startTime = time()
        self.iddfsPath = self.IDDFS(30)
        print(f"Iterative Deepening DFS Time: {time() - startTime}")
        startTime = time()
        self.manhattanPath = self.AStar(choice=True)
        print(f"A* using Manhattan Distance Time: {time() - startTime}")
        startTime = time()
        self.euclideanPath = self.AStar()
        print(f"A* using Euclidean Distance Time: {time() - startTime}")

    def BFS(self) -> list[BoardState]:
        queue: deque[tuple[BoardState, list[BoardState]]] = deque()
        visited: set[BoardState] = set()

        queue.append((self.boardState, [self.boardState]))

        while queue:
            currState, currPath = queue.popleft()

            if currState.checkSolved():
                return currPath

            visited.add(currState)
            for neighborState in currState.getNeighbors():
                if neighborState not in visited:
                    neighbor = (neighborState, currPath + [neighborState])
                    queue.append(neighbor)

    def DFS(self) -> list[BoardState]:
        stack: list[tuple[BoardState, list[BoardState]]] = []
        visited: set[BoardState] = set()

        stack.append((self.boardState, [self.boardState]))

        while stack:
            currState, currPath = stack.pop()

            if currState.checkSolved():
                return currPath

            visited.add(currState)
            for neighborState in currState.getNeighbors():
                if neighborState not in visited:
                    neighbor = (neighborState, currPath + [neighborState])
                    stack.append(neighbor)

    def IDDFS(self, maxDepth: int) -> list[BoardState]:
        for depth in range(maxDepth):
            result = self._depthLimitDFS(depth)
            if result:
                return result

    def _depthLimitDFS(self, maxDepth: int) -> list[BoardState]:
        stack: list[tuple[BoardState, list[BoardState]]] = []
        visited: set[BoardState] = set()

        stack.append((self.boardState, [self.boardState]))

        while stack:
            currState, currPath = stack.pop()

            if len(currPath) > maxDepth:
                continue

            if currState.checkSolved():
                return currPath

            visited.add(currState)
            for neighborState in currState.getNeighbors():
                if neighborState not in visited:
                    neighbor = (neighborState, currPath + [neighborState])
                    stack.append(neighbor)

    # false -> euclidean , true -> manhattan
    def AStar(self, choice: bool = False) -> list[BoardState]:
        heap: list[tuple[BoardState, list[BoardState]]] = []
        visited: set[BoardState] = set()

        if choice:
            self.boardState.manhattanDistance()
        else:
            self.boardState.euclideanDistance()

        heapq.heappush(heap, (self.boardState, [self.boardState]))

        while heap:
            currState, currPath = heapq.heappop(heap)

            if currState.checkSolved():
                return currPath

            visited.add(currState)
            for neighborState in currState.getNeighbors():
                if neighborState not in visited:
                    if choice:
                        neighborState.manhattanDistance()
                    else:
                        neighborState.euclideanDistance()

                    neighbor = (
                        neighborState,
                        currPath + [neighborState],
                    )
                    heapq.heappush(heap, neighbor)
