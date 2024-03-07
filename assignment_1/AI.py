from collections import deque
from BoardState import BoardState
import heapq
from time import time
from math import sqrt


class AI:
    goal: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, boardState):
        self.boardState: BoardState = boardState
        self.bfsPath = []
        self.dfsPath = []
        self.manhattanPath = []
        self.euclideanPath = []
        self.iddfsPath = []

    def checkSolved(boardState: BoardState) -> bool:
        return boardState.layout == AI.goal

    def solve(self, bfs=True, dfs=True, iddfs=True, manhattan=True, euclidean=True):
        if bfs:
            startTime = time()
            self.bfsPath = self.BFS()
            print(f"BFS Time: {time() - startTime}")

        if dfs:
            startTime = time()
            self.dfsPath = self.DFS()
            print(f"DFS Time: {time() - startTime}")

        if iddfs:
            startTime = time()
            self.iddfsPath = self.IDDFS(500)
            print(f"Iterative Deepening DFS Time: {time() - startTime}")

        if manhattan:
            startTime = time()
            self.manhattanPath = self.AStar(heuristic=AI.manhattanDistance)
            print(f"A* using Manhattan Distance Time: {time() - startTime}")

        if euclidean:
            startTime = time()
            self.euclideanPath = self.AStar(heuristic=AI.euclideanDistance)
            print(f"A* using Euclidean Distance Time: {time() - startTime}")

    def BFS(self) -> list[BoardState]:
        queue: deque[tuple[BoardState, list[BoardState]]] = deque()
        visited: set[BoardState] = set()

        queue.append((self.boardState, [self.boardState]))

        while queue:
            currState, currPath = queue.popleft()

            if AI.checkSolved(currState):
                return currPath

            visited.add(currState)
            for neighborState in currState.getNeighbors():
                if neighborState not in visited and neighborState not in queue:
                    neighbor = (neighborState, currPath + [neighborState])
                    queue.append(neighbor)

    def DFS(self) -> list[BoardState]:
        stack: list[tuple[BoardState, list[BoardState]]] = []
        visited: set[BoardState] = set()

        stack.append((self.boardState, [self.boardState]))

        while stack:
            currState, currPath = stack.pop()

            if AI.checkSolved(currState):
                return currPath

            visited.add(currState)
            for neighborState in currState.getNeighbors():
                if neighborState not in visited and neighborState not in stack:
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

            if AI.checkSolved(currState):
                return currPath

            visited.add(currState)
            for neighborState in currState.getNeighbors():
                if neighborState not in visited and neighborState not in stack:
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

            if AI.checkSolved(currState):
                return currPath

            visited.add(currState)
            for neighborState in currState.getNeighbors():
                if neighborState not in visited and neighborState not in heap:
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
