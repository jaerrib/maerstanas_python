def convert_num_to_row(num):
    rows = ["A", "B", "C", "D", "E", "F", "G"]
    return rows[num - 1]


def find_adjacent(row_number, col_number):
    """
    Returns assigned value for positions adjacent to a given board position
    """
    adjacent_positions = [
        [row_number - 1, col_number],
        [row_number, col_number - 1],
        [row_number, col_number + 1],
        [row_number + 1, col_number],
    ]
    return adjacent_positions


def check_player_hinges(board, row_number, col_number):
    """
    Evaluates the number of hinges a player move would have
    if played at a given board position
    """
    adjacent_positions = find_adjacent(row_number, col_number)
    hinges = 0
    for position in range(0, len(adjacent_positions)):
        row_to_check = adjacent_positions[position][0]
        col_to_check = adjacent_positions[position][1]
        position_check = board[row_to_check][col_to_check]
        if position_check[0] != 0:
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
        if position_check[0] == 3:
            hinges += 1
        elif position_check[0] == 1 or position_check[0] == 2:
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
        if board_value[0] == 3 or board_value[0] == 0:
            pass
        elif board_value[0] == 1 or board_value[0] == 2:
            if hinge_check(board, row_position, col_position) >= 3:
                return True
    return False


def change_player(data):
    if data["active_player"] == 1:
        data["active_player"] = 2
    elif data["active_player"] == 2:
        data["active_player"] = 1
    data["active_stone"] = 1
    return data


def check_default_stone(data, row, col):
    """
    Determines if a potential move would be valid by doing the following:
    (1) Checking if the coordinates are within the confines of the board
    (2) Checking if the position is occupied
    (3) Checking if the move would create 4 immediate hinges
    (4) Checking if the move would cause any adjacent stones to have more
    than 3 hinges
    """
    if 1 <= row < 9 and 1 <= col < 9:
        player_move = data["board"][row][col]
    else:
        # Invalid move - outside board confines
        return False
    if player_move[0] != 0:
        # Invalid move - space occupied
        return False
    else:
        if check_player_hinges(data["board"], row, col):
            # Invalid move - move would cause 4 immediate hinges
            return False
        elif check_adjacent_stones(data["board"], row, col):
            # Invalid move - an adjacent stone would have 4 hinges
            return False
        else:
            return True


def check_thunder_stone(data, row, col):
    """
    Determines if a potential move would be valid by doing the following:
    (1) Checking if the coordinates are within the confines of the board
    (2) Checking if the position is occupied
    """
    if 1 <= row < 9 and 1 <= col < 9:
        player_move = data["board"][row][col]
    else:
        # Invalid move - outside board confines
        return False
    # Return if the chosen space is occupied
    return player_move[0] == 0


def check_woden_stone(data, row, col):
    """
    Determines if a potential move would be valid by doing the following:
    (1) Checking if the coordinates are within the confines of the board
    (2) Checking if the position is occupied by an opponent's stone
    """
    if 1 <= row < 8 and 1 <= col < 8:
        player_move = data["board"][row][col]
    else:
        # Invalid move - outside board confines
        return False
    # Return if the chosen space is occupied by opponent's stone
    return player_move[1] != 0 and player_move[0] != data["active_player"]


def valid_move(data, row, col):
    if data["active_stone"] == 1:
        return check_default_stone(data, row, col)
    if data["active_stone"] == 2:
        return check_thunder_stone(data, row, col)
    if data["active_stone"] == 3:
        return check_woden_stone(data, row, col)


def check_score(board, score_type, player):
    """
    Evaluates the score of current board positions, first looping through the
    vertical hinges then the horizontal ones.
    """
    calculated_score: int = 0

    for row_index in range(1, 9):
        for col_index in range(0, 9):
            board_position = board[row_index][col_index]
            comparison_position = board[row_index - 1][col_index]
            if comparison_position[0] == player and board_position[0] == player:
                calculated_score += 1
            elif comparison_position[0] == 3 and board_position[0] == player:
                calculated_score += score_type
            elif comparison_position[0] == player and board_position[0] == 3:
                calculated_score += score_type

    for row_index in range(1, 9):
        for col_index in range(0, 9):
            board_position = board[row_index][col_index]
            comparison_position = board[row_index][col_index - 1]
            if comparison_position[0] == player and board_position[0] == player:
                calculated_score += 1
            elif comparison_position[0] == 3 and board_position[0] == player:
                calculated_score += score_type
            elif comparison_position[0] == player and board_position[0] == 3:
                calculated_score += score_type
    return calculated_score


def possible_thunder_stone_moves(data):
    possible_moves = []
    for row_index in range(1, 9):
        for col_index in range(1, 9):
            if check_thunder_stone(data, row_index, col_index):
                possible_moves.append([row_index, col_index])
    return possible_moves


def possible_woden_stone_moves(data):
    possible_moves = []
    for row_index in range(1, 9):
        for col_index in range(1, 9):
            if check_woden_stone(data, row_index, col_index):
                possible_moves.append([row_index, col_index])
    return possible_moves


def remaining_moves(board):
    """
    Cycles through board positions starting at A1 (1,1). If a position is
    a potentially valid move, it is appended to an array which is then used
    when the pseudo AI randomly selects its move.
    """
    possible_moves = []
    for row_index in range(1, 9):
        for col_index in range(1, 9):
            if board[row_index][col_index][0] != 0:
                pass
            else:
                if check_player_hinges(board, row_index, col_index):
                    pass
                elif check_adjacent_stones(board, row_index, col_index):
                    pass
                else:
                    possible_moves.append([row_index, col_index])
    return possible_moves


def update_score(data):
    data["score_p1"] = check_score(
        board=data["board"], score_type=data["scoring_type"], player=1
    )
    data["score_p2"] = check_score(
        board=data["board"], score_type=data["scoring_type"], player=2
    )
    return data


def determine_winner(score_p1, score_p2):
    if score_p1 == score_p2:
        result = "tie"
    elif score_p1 > score_p2:
        result = "player 1"
    else:
        result = "player 2"
    return result


def thunder_attack(data, row, col):
    adjacent_positions = find_adjacent(row, col)
    for position in adjacent_positions:
        if data["board"][position[0]][position[1]] != (3, 3):
            data["board"][position[0]][position[1]] = (0, 0)
    return data


def assign_move(data, row, col):
    if data["active_stone"] == 2:
        thunder_attack(data, row, col)
    if data["active_stone"] == 2 or data["active_stone"] == 3:
        data["special_stones"][f"player{data['active_player']}"].remove(
            data["active_stone"]
        )
    data["board"][row][col] = (data["active_player"], data["active_stone"])
    stones = ["standard stone", "thunder-stone", "Woden-stone"]
    played_stone = stones[data["active_stone"] - 1]
    data["move_list"].append(
        (
            data["active_player"],
            convert_num_to_row(col) + str(row) + " - " + played_stone,
        )
    )
    data = update_score(data)
    data = change_player(data)
    data["moves_left"] = remaining_moves(data["board"])
    return data


def change_stone(data, stone):
    data["active_stone"] = stone
    return data


def is_game_over(data):
    player1_has_special_stones = len(data["special_stones"]["player1"]) > 1
    player2_has_special_stones = len(data["special_stones"]["player2"]) > 1
    default_moves_are_left = remaining_moves(data["board"]) != []
    return (
        not player1_has_special_stones
        and not player2_has_special_stones
        and not default_moves_are_left
    )


def player_must_pass(data):
    player_num = str(data["active_player"])
    no_special_stones = len(data["special_stones"]["player" + player_num]) == 1
    return no_special_stones and data["moves_left"] == []
