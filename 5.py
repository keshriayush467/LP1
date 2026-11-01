n = int(input("Enter the no of queens: "))

board = [[0 for i in range(n)] for j in range(n)]

def safe(row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve(row):
    if row == n:
        return True

    for col in range(n):
        if safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False

board[0][0] = 1
if solve(0):
    print("\nN Queen Matrix is")
    for row in board:
        print(row)
else:
    print("Solution does not exist")