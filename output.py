def printOutput(board):
    outputFile = open("output.txt", 'w')
    for p in board:
        outputFile.write(str(p) + "\n")

    outputFile.close()
