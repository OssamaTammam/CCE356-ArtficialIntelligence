from Board import Board


def main():
    gameBoard = Board()
    gameBoard.state.layout = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    print("Current game board:")
    gameBoard.printState()

    bfsPath = gameBoard.BFS()
    print("BFS:")
    Board.printPath(bfsPath)

    gameBoard = Board()
    gameBoard.state.layout = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    dfsPath = gameBoard.DFS()
    print("DFS:")
    Board.printPath(dfsPath)

    gameBoard = Board()
    gameBoard.state.layout = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    manhattanPath = gameBoard.AStarManhattan()
    print("AStar Manhattan:")
    Board.printPath(manhattanPath)

    gameBoard = Board()
    gameBoard.state.layout = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    euclideanPath = gameBoard.AStarEuclidean()
    print("AStar Euclidean:")
    Board.printPath(euclideanPath)


if __name__ == "__main__":
    main()
