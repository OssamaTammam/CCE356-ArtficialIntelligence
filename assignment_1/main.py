from Board import Board


testLayout = [1, 2, 5, 3, 4, 0, 6, 7, 8]


def main():
    gameBoard = Board(layout=testLayout)
    gameBoard.printState()

    gameBoard.solve()
    gameBoard.printAiPaths()


if __name__ == "__main__":
    main()
