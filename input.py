board = []
def takeInput():
    inputFile = open("input.txt", 'r')
    for i in range(9):
        l = inputFile.readline()
        boardline = []
        for c in l:
            if c != ' ' and c != '\n':
                boardline.append(int(c))
        board.append(boardline)
    inputFile.close()
    return board
