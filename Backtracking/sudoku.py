def isSafe(board,row,col,num):
    for i in range(9):
        if(board[row][i]==num):
            return False
    
    for i in range(9):
        if(board[i][col]==num):
            return False
    box_row=(row//3)*3
    box_col=(col//3)*3
    for i in range(box_row,box_row+3):
        for j in range(box_col,box_col+3):
            if(board[i][j]==num):
                return False
    return True
def isEmpty(board):
    for i in range(9):
        for j in range(9):
            if(board[i][j]==0):
                return True,i,j
    return False,-1,-1
def SudokuSolver(board):
    empty, row, col = isEmpty(board)
    if not empty:
        return True
    for num in range(1,10):
        if isSafe(board,row,col,num):
            board[row][col]=num
            if SudokuSolver(board):
                return True
            board[row][col]=0
    return False
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
SudokuSolver(board)
print("board : ",board)