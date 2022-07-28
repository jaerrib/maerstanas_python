from os import system
import sys
import secrets

# Initializes board and values and creates the 9x9 grid
board = []
for row_num in range(9):
    row = []
    for col_num in range(9):
        row.append(0)
    board.append(row)

# Assigns an "E" to all edge positions for use in positional
# comparison functions
for col_num in range(9):
    board[0][col_num] = 'E'
    board[8][col_num] = 'E'
for row_num in range(1, 8):
    board[row_num][0] = 'E'
    board[row_num][8] = 'E'


def print_board(board_array):
    # Displays only the playable board positions, NOT the edges and
    # exchanges the numerical values for a dash or unicode characters.
    # This is for display purposes only to simulate stones on a game board.
    for row_index in range(1, 8):
        for col_index in range(1, 8):
            icons = ['-', '\u25CB', '\u25CF']
            icon = icons[board_array[row_index][col_index]]
            print(icon, end="")
        print()


def convert_row_to_num(character):
    # Converts player's letter input to a number usable by various functions
    # Other letters will return 0, which is outside confines of the board
    letter = character.upper()
    possible_rows = "ABCDEFG"
    if letter in possible_rows:
        return possible_rows.index(letter) + 1
    return 0


def check_player_hinges(row_number, col_number):
    # Determines adjacent stone values and assigns them to a list
    stone_above = board[row_number - 1][col_number]
    stone_left = board[row_number][col_number - 1]
    stone_right = board[row_number][col_number + 1]
    stone_below = board[row_number + 1][col_number]
    adjacent_stones = [stone_above, stone_left, stone_right, stone_below]

    # Counts the number of hinges a potential position would have
    hinges = 0
    for position in range(0, len(adjacent_stones)):
        position_check = adjacent_stones[position]
        if position_check != 0:
            hinges += 1
    if hinges > 3:
        return True
    else:
        return False


def hinge_check(row_number, col_number):
    # Determines adjacent stone values and assigns them to a list
    stone_above = board[row_number - 1][col_number]
    stone_left = board[row_number][col_number - 1]
    stone_right = board[row_number][col_number + 1]
    stone_below = board[row_number + 1][col_number]
    adjacent_stones = [stone_above, stone_left, stone_right, stone_below]

    # Counts the number of hinges each adjacent stone has    
    hinges = 0
    for i in range(0, len(adjacent_stones)):
        position_check = adjacent_stones[i]
        if position_check == 'E':
            hinges += 1
        elif position_check == 1 or position_check == 2:
            hinges += 1
        else:
            pass
    return hinges


def check_adjacent_stones(row_number, col_number):
    # Determines adjacent stone positions and assigns them to a list
    stone_above = [row_number - 1, col_number]
    stone_left = [row_number, col_number - 1]
    stone_right = [row_number, col_number + 1]
    stone_below = [row_number + 1, col_number]
    adjacent_stones = [stone_above, stone_left, stone_right, stone_below]

    # Counts the number of hinges each adjacent stone has
    # Vacant (value 0) and edge positions are ignored
    for i in range(0, len(adjacent_stones)):
        row_position = int(adjacent_stones[i][0])
        col_position = int(adjacent_stones[i][1])
        board_value = board[row_position][col_position]
        if board_value == 'E' or board_value == 0:
            pass
        elif board_value == 1 or board_value == 2:
            if hinge_check(row_position, col_position) >= 3:
                return True
    return False


def change_player(player):
    if player == 1:
        return 2
    elif player == 2:
        return 1


def valid_move(row_number, col_number, player):
    if 1 <= row_number < (len(board) - 1) \
            and 1 <= col_number < (len(board) - 1):
        player_move = board[row_number][col_number]
    else:
        # print("Invalid move. Outside board confines")
        # input("Press <Enter> to continue")
        return
    if player_move != 0:
        # print("Invalid move. Space occupied")
        # input("Press <Enter> to continue")
        return False
    else:
        if check_player_hinges(row_number, col_number):
            # print("Invalid move. Move would cause 4 immediate hinges.")
            # input("Press <Enter> to continue")
            return False
        elif check_adjacent_stones(row_number, col_number):
            # print("Invalid move. An adjacent stone would have 4 hinges.")
            # input("Press <Enter> to continue")
            return False
        else:
            board[row_number][col_number] = player
            return True


def check_score(player):
    calculated_score: int = 0

    # Scores all vertical hinges
    for row_index in range(1, len(board)):
        for col_index in range(0, len(board)):
            board_position = board[row_index][col_index]
            comparison_position = board[row_index - 1][col_index]
            if comparison_position == player \
                    and board_position == player:
                calculated_score += 1
            elif comparison_position == 'E' and board_position == player:
                calculated_score += 1
            elif board_position == 'E' and comparison_position == player:
                calculated_score += 1
            else:
                pass

    # Scores all horizontal hinges
    for row_index in range(1, (len(board))):
        for col_index in range(0, (len(board))):
            board_position = board[row_index][col_index]
            comparison_position = board[row_index][col_index - 1]
            if comparison_position == player \
                    and board_position == player:
                calculated_score += 1
            elif comparison_position == 'E' and board_position == player:
                calculated_score += 1
            elif board_position == 'E' and comparison_position == player:
                calculated_score += 1
            else:
                pass
    return calculated_score


def viable_moves():
    # Cycles through board positions starting at 1,1. If a position is
    # valid, viable_moves is True play is allowed to continue. If a
    # position is not valid, the next position is assessed.
    for row_index in range(1, len(board)):
        for col_index in range(1, len(board)):
            if board[row_index][col_index] != 0:
                pass
            else:
                if check_player_hinges(row_index, col_index):
                    pass
                elif check_adjacent_stones(row_index, col_index):
                    pass
                else:
                    return True


def computer_move(computer_player):
    # Pseudo AI placeholder using random moves
    valid = False
    while not valid:
        rand_row = secrets.randbelow(7) + 1
        rand_col = secrets.randbelow(7) + 1
        valid = valid_move(rand_row, rand_col, computer_player)
    # converted_row = "ABCDEFG"[rand_row - 1]
    # print("Computer played {}{}".format(converted_row, rand_col))
    return change_player(computer_player)


def one_player_game():
    active_player = 1
    # Main game loop
    while viable_moves():
        system('clear')

        print_board(board)

        for player_number in (1, 2):
            score = check_score(player_number)
            if player_number == 1:
                print("Player {}'s score: {}".format(player_number, score))
            else:
                print("Computer's score: {}".format(score))
        print()

        if active_player == 1:
            print("Player {}'s turn".format(active_player))
            entered_move = (
                input("Enter row letter and column number - with no spaces - to "
                      "place your stone: ")
            )
            move_row = convert_row_to_num(entered_move[0])
            move_col = int(entered_move[1])
            if valid_move(move_row, move_col, active_player):
                active_player = change_player(active_player)
        else:
            # print("Computer played ", computer_move(active_player))
            computer_move(active_player)
            active_player = change_player(active_player)
            input("Press <Enter> to continue")
        # Additional code assigns active player number to the unused board
        # position at 0,0 for a planned game save/load feature
        # board[0][0] = player
    if check_score(1) == check_score(2):
        print("It's a tie!")
    elif check_score(1) > check_score(2):
        print("Player 1 wins!")
    else:
        print("Computer wins!")


def two_player_game():
    active_player = 1
    # Main game loop
    while viable_moves():
        system('clear')

        print_board(board)

        for player_number in (1, 2):
            score = check_score(player_number)
            print("Player {}'s score: {}".format(player_number, score))
        print()

        print("Player {}'s turn".format(active_player))
        entered_move = (
            input("Enter row letter and column number - with no spaces - to "
                  "place your stone: ")
        )
        move_row = convert_row_to_num(entered_move[0])
        move_col = int(entered_move[1])
        if valid_move(move_row, move_col, active_player):
            active_player = change_player(active_player)
            # Additional code assigns active player number to the unused board
            # position at 0,0 for a planned game save/load feature
            # board[0][0] = player
    if check_score(1) == check_score(2):
        print("It's a tie!")
    elif check_score(1) > check_score(2):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


num_players = input("1 or 2 player game? ")
if num_players == '1':
    one_player_game()
elif num_players == '2':
    two_player_game()
else:
    print("Invalid entry")
sys.exit()
