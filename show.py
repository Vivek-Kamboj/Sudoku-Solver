from tkinter import *


def show(board):
    N = 9
    UNASSIGNED = 0



    root = Tk()
    root.title("Sudoku Solver")

    title = Label(root, text="Sudoku Solver", font=('Arial', 30, 'bold'))

    frame = Frame(root)

    for i in range(N):
        for j in range(N):
            if board[i][j] == UNASSIGNED:
                e = Entry(frame, borderwidth=2, relief="groove", width=3, fg='blue', font=('Arial', 16, 'bold'))
                e.grid(row=i, column=j)
                # e.insert(END, board[i][j])
            else:
                Label(frame, text=board[i][j], borderwidth=2, relief="groove", width=3, fg='black',
                      font=('Arial', 16, 'bold')).grid(row=i, column=j)
    title.pack()
    frame.pack()
    root.mainloop()