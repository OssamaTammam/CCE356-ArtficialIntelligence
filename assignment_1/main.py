from Board import Board


def main():
    # gameBoard = Board()
    # gameBoard.state.layout = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    # bfsPath = gameBoard.BFS()
    # print("BFS Path:")
    # Board.printPath(bfsPath)
    gameBoard = Board()
    gameBoard.state.layout = [1, 2, 0, 3, 4, 5, 6, 7, 8]
    dfsPath = gameBoard.AStar()
    print("AStar Path:")
    Board.printPath(dfsPath)


if __name__ == "__main__":
    main()
