from os import system

clear = lambda: system('clear')

# Initialize board positions, scores and active player
board = []
for i in range(9):
    row = []
    for j in range(9):
        row.append(0)
    board.append(row)

# Assign edges
for i in range(9):
    board[0][i] = 'E'
    board[8][i] = 'E'
for i in range(1, 8):
    board[i][0] = 'E'
    board[i][8] = 'E'

scoreP1 = 0
scoreP2 = 0
activePlayer = 1
viableMoves = True

def convert_row_to_num(character):
    letters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for i in range(0, len(letters)):
        if character == letters[i]:
            return (i + 1)

def check_player_hinges(moveRow, moveCol):
    stoneAbove = board[moveRow - 1][moveCol]
    stoneLeft = board[moveRow][moveCol - 1]
    stoneRight = board[moveRow][moveCol + 1]
    stoneBelow = board[moveRow + 1][moveCol]
    adjacent_stones = [stoneAbove, stoneLeft, stoneRight, stoneBelow]
    hinges = 0
    for i in range(0, len(adjacent_stones)):
        positionCheck = adjacent_stones[i]
        if positionCheck != 0:
            hinges += 1
    if hinges > 3:
        return True
    else:
        return False

def hinge_check(row, col):
    stoneAbove = board[row - 1][col]
    stoneLeft = board[row][col - 1]
    stoneRight = board[row][col + 1]
    stoneBelow = board[row + 1][col]
    adjacent_stones = [stoneAbove, stoneLeft, stoneRight, stoneBelow]
    hinges = 0
    for i in range(0, len(adjacent_stones)):
        positionCheck = adjacent_stones[i]
        if positionCheck == 'E':
            hinges += 1
        elif positionCheck == 1 or positionCheck == 2:
            hinges += 1
        else:
            pass
    return hinges

def check_adjacent_stones(moveRow, moveCol):
    stoneAbove = [moveRow - 1, moveCol]
    stoneLeft = [moveRow, moveCol - 1]
    stoneRight = [moveRow, moveCol + 1]
    stoneBelow = [moveRow + 1, moveCol]
    adjacent_stones = [stoneAbove, stoneLeft, stoneRight, stoneBelow]
    for i in range(0, len(adjacent_stones)):
        row = int(adjacent_stones[i][0])
        col = int(adjacent_stones[i][1])
        boardValue = board[row][col]
        if boardValue == 'E' or boardValue == 0:
            pass
        elif boardValue == 1 or boardValue == 2:
            if hinge_check(row, col) >= 3:
                return True
    return False

def change_player(activePlayer):
    if activePlayer == 1:
        return 2
    elif activePlayer == 2:
        return 1

def validate_move(moveRow, moveCol, activePlayer):
    if moveRow >= 1 and moveRow < (len(board)-1) and moveCol >= 1 and moveCol < (len(board)-1):
        playerMove = board[moveRow][moveCol]
    else:
        print("Invalid move. Outside board confines")
        input("Press <Enter> to continue")
        return
    if playerMove != 0:
        print("Invalid move. Space occupied")
        input("Press <Enter> to continue")
        return False
    else:
        if check_player_hinges(moveRow, moveCol):
            print("Invalid move. Move would cause 4 immediate hinges.")
            input("Press <Enter> to continue")
            return False
        elif check_adjacent_stones(moveRow, moveCol):
            print("Invalid move. An adjacent stone would have 4 hinges.")
            input("Press <Enter> to continue")
            return False
        else:
            #print("Valid")
            board[moveRow][moveCol] = activePlayer          # Assigns player input to board position
            return True

def check_score(playerNumber):
    score = 0
    # check vertical hinges
    for row in range(1, len(board)):
        for col in range(0, len(board)):
            boardPosition = board[row][col]
            comparisonPosition = board[row - 1][col]
            if comparisonPosition == playerNumber and boardPosition == playerNumber:
                score += 1
            elif comparisonPosition == 'E' and boardPosition == playerNumber:
                score += 1
            elif boardPosition == 'E' and comparisonPosition == playerNumber:
                score += 1
            else:
                pass

# check horizontal hinges
    for row in range(1, (len(board))):
        for col in range(0, (len(board))):
            boardPosition = board[row][col]
            comparisonPosition = board[row][col-1]
            if comparisonPosition == playerNumber and boardPosition == playerNumber:
                score += 1
            elif comparisonPosition == 'E' and boardPosition == playerNumber:
                score += 1
            elif boardPosition == 'E' and comparisonPosition == playerNumber:
                score += 1
            else:
                pass
    return score

def viableMoves():
    score = 0
    for row in range(1, len(board)):
        for col in range(1, len(board)):
            if board[row][col] != 0:
                pass
            else:
                if check_player_hinges(row, col):
                    pass
                elif check_adjacent_stones(row, col):
                    pass
                else:
                    return True

# Main loop



while viableMoves():
    clear()

    # displays only usable board positions - NOT the edges
    for i in range(1, 8):
        for j in range(1, 8):
            print(board[i][j], end="")
        print()

    for playerNumber in (1, 2):
        print("Player", playerNumber, "score:", check_score(playerNumber))
    print()

    print("Player ", activePlayer, "'s turn")
    enteredMove = (input("Enter row letter and column number - with no spaces - to place your stone: "))      # Accept input from player for stone placement
    moveRow = convert_row_to_num(enteredMove[0])
    moveCol = int(enteredMove[1])
    if validate_move(moveRow, moveCol, activePlayer):
        # Change active player
        activePlayer = change_player(activePlayer)

if check_score(1) == check_score(2):
    print("It's a tie!")
elif check_score(1) > check_score(2):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")