from collections import deque
from BoardState import BoardState
import heapq
from time import time
from math import sqrt


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
        self.manhattanPath = self.AStar(heuristic=AI.manhattanDistance)
        print(f"A* using Manhattan Distance Time: {time() - startTime}")

        startTime = time()
        self.euclideanPath = self.AStar(heuristic=AI.euclideanDistance)
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

    def AStar(self, heuristic: callable) -> list[BoardState]:
        heap: list[tuple[int, BoardState, list[BoardState]]] = []
        visited: set[BoardState] = set()

        # tuple (cost,state,path)
        heapq.heappush(
            heap, (0 + heuristic(self.boardState), self.boardState, [self.boardState])
        )

        while heap:
            currCost, currState, currPath = heapq.heappop(heap)

            if currState.checkSolved():
                return currPath

            visited.add(currState)
            for neighborState in currState.getNeighbors():
                if neighborState not in visited:
                    cost = currCost + 1 + heuristic(neighborState)
                    neighbor = (
                        cost,
                        neighborState,
                        currPath + [neighborState],
                    )
                    heapq.heappush(heap, neighbor)

    def manhattanDistance(boardState: BoardState) -> int:
        manhattanDistance = 0

        for i in range(len(boardState.layout)):
            manhattanDistance += abs((boardState.layout[i] // 3) - i // 3) + abs(
                (boardState.layout[i] % 3) - i % 3
            )

        return manhattanDistance

    def euclideanDistance(boardState: BoardState) -> int:
        euclideanDistance = 0

        for i in range(len(boardState.layout)):
            euclideanDistance += sqrt(
                ((boardState.layout[i] // 3) - i // 3) ** 2
                + ((boardState.layout[i] % 3) - i % 3) ** 2
            )

        return euclideanDistance
