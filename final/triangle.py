
def triangle(board):
    F = [[0] * len(board[i]) for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j - 1 >= 0:
                if j < len(board[i]) - 1:
                    better_move = min(F[i - 1][j - 1], F[i - 1][j])
                else:
                    better_move = F[i - 1][j - 1]
            else:
                better_move = F[i - 1][j]
            F[i][j] = better_move + board[i][j]

    return min(F[-1])


if __name__ == "__main__":
    board = [[2],[5,4],[1,4,7],[8,6,9,6]]
    # board = [[1]]
    # board = [[1], [2, 3], [7, 5, 9]]
    print(triangle(board))


