# https://leetcode.com/problems/surrounded-regions/
"""
Discription of question in above link
"""


def solve(board):

    if(len(board) == 0 or len(board[0]) == 0):
        return

    result = []
    row = len(board)
    column = len(board[0])

    # For first and last row
    for i in range(0, row):
        if(board[i][0] == 'O'):
            boundaryDFS(board, i, 0)
        if(board[i][column-1] == 'O'):
            boundaryDFS(board, i, column-1)

    # For first and last column
    for j in range(0, column):
        if(board[0][j] == 'O'):
            boundaryDFS(board, 0, j)
        if(board[row-1][j] == 'O'):
            boundaryDFS(board, row-1, j)
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if(board[i][j] == 'O'):
                board[i][j] = 'X'
            if(board[i][j] == '*'):
                board[i][j] = 'O'

    return board


def boundaryDFS(board, i, j):
    if(i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1):
        return

    if(board[i][j] == 'O'):
        board[i][j] = '*'

    if(i > 0 and board[i-1][j] == 'O'):
        boundaryDFS(board, i-1, j)
    if(i < len(board)-1 and board[i+1][j] == 'O'):
        boundaryDFS(board, i+1, j)
    if(j > 0 and board[i][j-1] == 'O'):
        boundaryDFS(board, i, j-1)
    if(j < len(board[0])-1 and board[i][j+1] == 'O'):
        boundaryDFS(board, i, j+1)
    return True
#  Driver program to test the above function


def main():
    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]
    print(solve(board))


if __name__ == "__main__":
    main()
