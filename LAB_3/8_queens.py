N = 8

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve(board, row):
    if row == N:
        print_board(board)
        return True
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve(board, row + 1):
                return True
    return False

def print_board(board):
    for row in range(N):
        line = ['.'] * N
        line[board[row]] = 'Q'
        print(' '.join(line))
    print()

board = [-1] * N
solve(board, 0)
