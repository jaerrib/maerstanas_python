from array import *

# Initialize board positions, scores and active player

# Board initialization

board = []
for i in range(9):
    row = []
    for j in range(9):
        row.append(0)
    board.append(row)

scoreP1 = 0
scoreP2 = 0
activePlayer = 1
viableMoves = True

# Main loop

# Determine whose turn it is

# Accept input from player for stone placement

while viableMoves:
    # display valid board positions - NOT edges
    for i in range(1,8):
        for j in range(1 ,8):
            print(board[j][i], end="")
        print()

    print("Player ", activePlayer, "'s turn")
    move = (input("Enter row and column numbers - with no spaces - to place your stone: "))
    row = int(move[0])
    col = int(move[1])
    print(row, col, "Player", activePlayer)
    board[row][col] = activePlayer

# Assign player input to board position

# Update score display

# Change active player
    if activePlayer == 1:
        activePlayer = 2
    elif activePlayer == 2:
        activePlayer = 1

# Determine if there are any viable moves left

# If yes, then repeat loop

# If no, then display winner based on score

# Ask to play again or quit