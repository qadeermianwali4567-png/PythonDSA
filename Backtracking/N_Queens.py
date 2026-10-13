def solve(n):
    """
    Solve the N-Queens problem and return all distinct solutions.

    :param n: The number of queens and the size of the chessboard (n x n).
    :return: A list of solutions, where each solution is represented as a list of strings.
    """
    def is_not_under_attack(row, col):
        for prev_row in range(row):
            print("prev row : ",prev_row)
            if (cols[prev_row] == col or
                abs(cols[prev_row] - col) == abs(prev_row - row)):
                return False
        return True

    def place_queen(row):
       
        if row == n:
            board = []
            for r in range(n):
                line = ['.'] * n
                line[cols[r]] = 'Q'
                board.append(''.join(line))
            solutions.append(board)
            return
        
        for col in range(n):
            
            issafe=is_not_under_attack(row, col)
            print("col in loop : ",col," row : ",row," issafe : ",issafe," cols : ",cols," n : ",n," solutions : ",solutions," board : ",board if row==n else "N/A",)
            if issafe:
                cols[row] = col
                place_queen(row + 1)
                cols[row] = -1  # Backtrack

    solutions = []
    cols = [-1] * n  # cols[i] will hold the column index of the queen in row i
    place_queen(0)
    return solutions
print(solve(4))
