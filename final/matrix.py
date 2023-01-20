
def matrix(board):
    F = [[0] * len(board[0]) for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            try:
                better_move = min(F[i - 1][j], F[i - 1][j - 1], F[i - 1][j + 1])
            except IndexError:
                if j - 1 >= 0:
                    better_move = min(F[i - 1][j], F[i - 1][j - 1])
                else:
                    better_move = F[i - 1][j]
            F[i][j] = better_move + board[i][j]

    return min(F[-1])


if __name__ == "__main__":
    # board = [[1,2,3],[4,5,6],[7,0,2]]
    # board = [[1,2,3]]
    # board = [[1]]
    board = [[1,2,3,0],[4,5,1,6],[7,0,2,0]]
    print(matrix(board))

