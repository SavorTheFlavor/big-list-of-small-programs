board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

def printBoard():
    print(f'''\n      0   1   2
    0 {board[0][0]} | {board[0][1]} | {board[0][2]}
      ---------
    1 {board[1][0]} | {board[1][1]} | {board[1][2]}
      ---------
    2 {board[2][0]} | {board[2][1]} | {board[2][2]}
    \n''')

def playerTurn(sign):
    print(f"---- {sign}'s turn ----")
    while True:
        # Get player input
        row = int(input('Row > '))
        col = int(input('Column > '))

        # Check if choice is valid index
        if row in range(0,3) and col in range(0,3):
            # Check if choice space is empty
            if board[row][col] == ' ':
                board[row][col] = sign
                break
            else:
                print('---- Invalid position ----')
                continue
        else:
            print('---- Invalid position ----')
            continue

def checkBoard(sign):
    # Rows
    for row in range(len(board)):
        if(board[row][0] + board[row][1] + board[row][2] == sign*3):
            print(f'{sign} wins')
            return(True)
    # Columns
    for col in range(len(board)):
        if(board[0][col] + board[1][col] + board[2][col] == sign*3):
            print(f'{sign} wins')
            return(True)
    # Diagonal
    if(board[0][0] + board[1][1] + board[2][2] == sign*3):
        print(f'{sign} wins')
        return(True)
    if(board[2][0] + board[1][1] + board[0][2] == sign*3):
        print(f'{sign} wins')
        return(True)


    # Check if board is full, then draw
    filled_rows = 0
    for i in range(len(board)):
        if ' ' not in board[i]:
            filled_rows += 1
    if filled_rows == 3:
        print("It's a draw")
        return(True)

printBoard()
while True:
    playerTurn('X')
    printBoard()
    if checkBoard('X') == True:
        break

    playerTurn('O')
    printBoard()
    if checkBoard('O') == True:
        break