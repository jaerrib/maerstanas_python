import secrets
from pygame import mixer

mixer.init()
invalid_move = mixer.Sound("sound/invalid.ogg")

def convert_row_to_num(character):
    """
    Converts player's letter input to a number usable by various functions.
    Other letters will return 0, which is outside confines of the board.
    """
    letter = character.upper()
    possible_rows = "ABCDEFG"
    if letter in possible_rows:
        return possible_rows.index(letter) + 1
    return 0


def find_adjacent(row_number, col_number):
    """
    Returns assigned value for positions adjacent to a given board position
    """
    adjacent_positions = [
        [row_number - 1, col_number],
        [row_number, col_number - 1],
        [row_number, col_number + 1],
        [row_number + 1, col_number]
    ]
    return adjacent_positions


def check_player_hinges(board, row_number, col_number):
    """
    Evaluates the number of hinges a player move would have
    if played at a given board position
    """
    adjacent_positions = find_adjacent(row_number, col_number)
    # Counts the number of hinges a potential position would have
    hinges = 0
    for position in range(0, len(adjacent_positions)):
        row_to_check = adjacent_positions[position][0]
        col_to_check = adjacent_positions[position][1]
        position_check = board[row_to_check][col_to_check]
        if position_check != 0:
            hinges += 1
    if hinges > 3:
        return True
    else:
        return False


def hinge_check(board, row_number, col_number):
    """
    Counts the number of hinges a stone at a given position has
    """
    adjacent_positions = find_adjacent(row_number, col_number)
    hinges = 0
    for position in range(0, len(adjacent_positions)):
        row_to_check = adjacent_positions[position][0]
        col_to_check = adjacent_positions[position][1]
        position_check = board[row_to_check][col_to_check]
        if position_check == 3:
            hinges += 1
        elif position_check == 1 or position_check == 2:
            hinges += 1
    return hinges


def check_adjacent_stones(board, row_number, col_number):
    """
    Determines if a move made at a given board position would cause any
    adjacent stones to have more than 3 hinges. Edge and empty/vacant board
    positions are ignored as they would zero hinges.
    """
    adjacent_positions = find_adjacent(row_number, col_number)
    # Counts the number of hinges each adjacent stone has
    # Open (value 0) and edge (value 3) positions are ignored
    for i in range(0, len(adjacent_positions)):
        row_position = int(adjacent_positions[i][0])
        col_position = int(adjacent_positions[i][1])
        board_value = board[row_position][col_position]
        if board_value == 3 or board_value == 0:
            pass
        elif board_value == 1 or board_value == 2:
            if hinge_check(board, row_position, col_position) >= 3:
                return True
    return False


def change_player(player):
    if player == 1:
        return 2
    elif player == 2:
        return 1


def valid_move(board, row_number, col_number):
    """
    Determines if a potential move would be valid by doing the following:
    (1) Checking if the coordinates are within the confines of the board
    (2) Checking if the position is occupied
    (3) Checking if the move would create 4 immediate hinges
    (4) Checking if the move would cause any adjacent stones to have more
    than 3 hinges
    If the move is valid, the player number is assigned to the board position
    """
    if 1 <= row_number < 9 \
            and 1 <= col_number < 9:
        player_move = board[row_number][col_number]
    else:
        # Invalid move - outside board confines
        mixer.Sound.play(invalid_move)
        return False
    if player_move != 0:
        # Invalid move - space occupied
        mixer.Sound.play(invalid_move)
        return False
    else:
        if check_player_hinges(board, row_number, col_number):
            # Invalid move - move would cause 4 immediate hinges
            mixer.Sound.play(invalid_move)
            return False
        elif check_adjacent_stones(board, row_number, col_number):
            # Invalid move - an adjacent stone would have 4 hinges
            mixer.Sound.play(invalid_move)
            return False
        else:
            return True


def check_score(board, player):
    """
    Evaluates the score of current board positions, first looping through the
    vertical hinges then the horizontal ones.
    """
    calculated_score: int = 0

    # Scores all vertical hinges
    for row_index in range(1, 9):
        for col_index in range(0, 9):
            board_position = board[row_index][col_index]
            comparison_position = board[row_index - 1][col_index]
            if comparison_position == player \
                    and board_position == player:
                calculated_score += 1
            elif comparison_position == 3 and board_position == player:
                calculated_score += 1
            elif board_position == 3 and comparison_position == player:
                calculated_score += 1

    # Scores all horizontal hinges
    for row_index in range(1, 9):
        for col_index in range(0, 9):
            board_position = board[row_index][col_index]
            comparison_position = board[row_index][col_index - 1]
            if comparison_position == player \
                    and board_position == player:
                calculated_score += 1
            elif comparison_position == 3 and board_position == player:
                calculated_score += 1
            elif board_position == 3 and comparison_position == player:
                calculated_score += 1
    return calculated_score


def viable_moves(board):
    """
    Cycles through board positions starting at A1 (1,1). If a position is
    valid, viable_moves is True and play is allowed to continue. If a
    position is not valid, the next position is assessed until the entire
    board has been checked.
    """
    for row_index in range(1, 9):
        for col_index in range(1, 9):
            if board[row_index][col_index] != 0:
                pass
            else:
                if check_player_hinges(board, row_index, col_index):
                    pass
                elif check_adjacent_stones(board, row_index, col_index):
                    pass
                else:
                    return True


def remaining_moves(board):
    """
    Cycles through board positions starting at A1 (1,1). If a position is
    a potentially valid move, it is appended to an array which is then used
    when the pseudo AI randomly selects its move.
    """
    possible_moves = []
    for row_index in range(1, 9):
        for col_index in range(1, 9):
            if board[row_index][col_index] != 0:
                pass
            else:
                if check_player_hinges(board, row_index, col_index):
                    pass
                elif check_adjacent_stones(board, row_index, col_index):
                    pass
                else:
                    possible_moves.append([row_index, col_index])
    return possible_moves


def determine_winner(board):
    score_p1 = check_score(board, 1)
    score_p2 = check_score(board, 2)
    if score_p1 == score_p2:
        result = "tie"
    elif score_p1 > score_p2:
        result = "player 1"
    else:
        result = "player 2"
    return result, score_p1, score_p2


def assign_move(board, row, col, player):
    board.data[row][col] = player
    key = ""+str(len(board.move_list))+""
    board.move_list[key] = [row, col, player]


def computer_move(board):
    """
    Pseudo AI placeholder that generates random moves for computer player
    """
    comp_move = secrets.choice(remaining_moves(board))
    row, col = comp_move[0], comp_move[1]
    return row, col
