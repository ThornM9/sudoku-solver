mainBoard = []
testBoard = []
allPotentials = {}
positionList = []
def collectBoard():
    global mainBoard, squareSize
    print("""Sudoku Solver By Thornton Mills\n
    Input your board as an array of arrays. Each array within the main array\n
    should be a row of the board. Each unknown square should be labelled as an 'x' \n
    Secondly, input the length of a side of a square in the board. The total \n
    width/height of the board should be a multiple of this number.""")
    mainBoard = input('Enter the board:')

    # CONDITIONS THE BOARD MUST MEET
    # Check board is an array
    try:
        mainBoard = eval(mainBoard)
    except:
        print("Input was not an array")
        return False

    boardWidth = len(mainBoard[0])
    # Check the board is a square
    if boardWidth != len(mainBoard):
        print("The width of the rows was not equal to the height of the board")
    # Check rows are equal length 
    for row in mainBoard:
        if len(row) != boardWidth:
            print("The width of all rows were not equal")
            return False

    squareSize = int(input('Enter the length of a square side:'))
    # Check width of board is a multiple of squaresize
    if (boardWidth % squareSize) != 0:
        print("Board size was not a multiple of square size")
        return False
    
    return True

def sudokuSolver():
    global mainBoard, squareSize, allPotentials, testBoard
    success = collectBoard()
    boardWidth = len(mainBoard)
    testBoard = mainBoard
    getUnknownPositions()
    recursiveSolve(positionList[0])

def recursiveSolve(positionKey):
    global testBoard, positionList
    index = positionList.index(positionKey)
    i = int(positionKey.split("-")[0])
    j = int(positionKey.split("-")[1])
    possibleSolutions = getPossibleSolutions(testBoard,i,j)
    print("\nPossible Solutions for " + positionKey + ": " + str(possibleSolutions))
    if len(possibleSolutions) == 0:
        print("No solution found. Backtracking")
        # reset the solution we're trying
        testBoard[i][j] = 'x'
        lastPosition = positionList[index-1]
        i = int(lastPosition.split("-")[0])
        j = int(lastPosition.split("-")[1])
        testBoard[i][j] = 'x'
        return False
    for solution in possibleSolutions:
        print("Trying solution: " + str(solution))
        testBoard[i][j] = solution
        if (index == len(positionList)):
            print("Board Solved: " + str(testBoard))
        else:
            if index > (len(positionList)-2):
                print(str(testBoard))
                return True
            success = recursiveSolve(positionList[index+1])
            if not success:
                testBoard[i][j] = 'x'
                continue
            else:
                return True

def getUnknownPositions():
    global mainBoard, allPotentials, positionList
    # i is a row
    for i in range(len(mainBoard)):
        # j is a column
        for j in range(len(mainBoard)):
            if mainBoard[i][j] == 'x':
                possibleSolutions = getPossibleSolutions(mainBoard,i,j)
                key = str(i) + "-" + str(j)
                allPotentials[key] = possibleSolutions
                positionList.append(key)

def getPossibleSolutions(board,i,j):
    boardWidth = len(board)
    possibleSolutions = []
    rowNums = board[i]
    #print("Row numbers: " + str(rowNums))
    columnNums = []
    for l in range(boardWidth):
        columnNums.append(board[l][j])
    #print("Column numbers: " + str(columnNums))
    squareNums = []
    # FIND THE SQUARE IT'S IN
    if i/squareSize < 1 and j/squareSize <1:
        square = 1
        for m in range(squareSize):
            for n in range(squareSize):
                if board[m][n] != 'x':
                    squareNums.append(board[m][n])
    elif i/squareSize < 1 and j/squareSize <2:
        square = 2
        for m in range(squareSize):
            for n in range(squareSize, squareSize*2):
                if board[m][n] != 'x':
                    squareNums.append(board[m][n])
    elif i/squareSize < 1 and j/squareSize <3:
        square = 3
        for m in range(squareSize):
            for n in range(squareSize*2, squareSize*3):
                if board[m][n] != 'x':
                    squareNums.append(board[m][n])
    elif i/squareSize < 2 and j/squareSize <1:
        square = 4
        for m in range(squareSize, squareSize*2):
            for n in range(squareSize):
                if board[m][n] != 'x':
                    squareNums.append(board[m][n])
    elif i/squareSize < 2 and j/squareSize <2:
        square = 5
        for m in range(squareSize, squareSize*2):
            for n in range(squareSize, squareSize*2):
                if board[m][n] != 'x':
                    squareNums.append(board[m][n])
    elif i/squareSize < 2 and j/squareSize <3:
        square = 6
        for m in range(squareSize, squareSize*2):
            for n in range(squareSize*2, squareSize*3):
                if board[m][n] != 'x':
                    squareNums.append(board[m][n])
    elif i/squareSize < 3 and j/squareSize <1:
        square = 7
        for m in range(squareSize*2, squareSize*3):
            for n in range(squareSize):
                if board[m][n] != 'x':
                    squareNums.append(board[m][n])
    elif i/squareSize < 3 and j/squareSize <2:
        square = 8
        for m in range(squareSize*2, squareSize*3):
            for n in range(squareSize, squareSize*2):
                if board[m][n] != 'x':
                    squareNums.append(board[m][n])
    elif i/squareSize < 3 and j/squareSize <3:
        square = 9
        for m in range(squareSize*2, squareSize*3):
            for n in range(squareSize*2, squareSize*3):
                if board[m][n] != 'x':
                    squareNums.append(board[m][n])
    
    #print("Current Square: " + str(square))
    #print("Numbers in current square: " + str(squareNums))
    for x in range(1, squareSize**2 + 1):
        if (x not in rowNums) and (x not in columnNums) and (x not in squareNums):
            possibleSolutions.append(x)
    return possibleSolutions

sudokuSolver()
