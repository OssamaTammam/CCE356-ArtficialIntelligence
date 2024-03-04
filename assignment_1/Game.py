from queue import Queue
from collections import deque


def BFS(self):
    visitedStates = set()
    queue = deque
    queue.put((self.currBoard.state, []))  # (state, path)

    while not queue.empty():
        state, path = queue.get()
        visitedStates.add(state)
