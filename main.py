import input
import solve
import show
import output



def main():
    board = input.takeInput()
    solve.solve(board)
    show.show(board)
    output.printOutput(board)

main()
