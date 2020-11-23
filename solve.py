N = 9
UNASSIGNED = 0
board = []


def solve_sudoku():
    find, row, col = find_unassigned()
    if find == False:
        return True
    for num in range(1, 10):
        if is_safe(row, col, num):
            board[row][col] = num
            if solve_sudoku():
                return True
            board[row][col] = UNASSIGNED

    return False


def find_unassigned():
    for i in range(9):
        for j in range(9):
            if board[i][j] == UNASSIGNED:
                return True, i, j
    return False, 10, 10


def is_safe(row, col, num):
    return used_in_row(row, num) == False & \
           used_in_column(col, num) == False & \
           used_in_sub_board(row, col, num) == False & \
           board[row][col] == UNASSIGNED


def used_in_row(row, num):
    for i in range(9):
        if board[row][i] == num:
            return True
    return False


def used_in_column(column, num):
    for i in range(9):
        if board[i][column] == num:
            return True
    return False


def used_in_sub_board(row, col, num):
    r = row // 3
    c = col // 3
    for i in range(3):
        for j in range(3):
            if board[i + r][j + c] == num:
                return True
    return False


def print_board():
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print("")


def solve(sudoku):
    global board
    board = sudoku
    if solve_sudoku():
        print_board()
    else:
        print("No Solution Exist!!")
