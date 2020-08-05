from tkinter import *
import solve

N = 9
UNASSIGNED = 0
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
board = solve.board

root = Tk()
root.title("Sudoku Solver")

title=Label(root, text="Sudoku Solver", font=('Arial', 30, 'bold'))

frame=Frame(root)

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            e = Entry(frame, borderwidth=2, relief="groove", width=3, fg='blue', font=('Arial', 16, 'bold'))
            e.grid(row=i, column=j)
            # e.insert(END, board[i][j])
        else:
            Label(frame, text=board[i][j], borderwidth=2, relief="groove", width=3, fg='black',
                  font=('Arial', 16, 'bold')).grid(row=i, column=j)
title.pack()
frame.pack()
root.mainloop()
