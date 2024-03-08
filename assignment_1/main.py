from Board import Board


testLayout = [1, 2, 3, 4, 5, 6, 7, 8, 0]


def main():
    gameBoard = Board(layout=testLayout)
    gameBoard.printState()

    gameBoard.solve(dfs=False, bfs=False)
    gameBoard.printAiPaths()


if __name__ == "__main__":
    main()
