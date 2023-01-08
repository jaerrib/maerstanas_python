from copy import deepcopy
import secrets

player_list = ["Computer", "Computer"]


def assign_result_value(result):
    if result == "tie":
        return 1
    elif result == "player 1":
        return -2
    elif result == "player 2":
        return 4


def computer_move(current_game):
    comp_move = secrets.choice(current_game.remaining_moves())
    row, col = comp_move[0], comp_move[1]
    return row, col


def sim_game_loop(current_board, players):
    temp_game = deepcopy(current_board)
    if temp_game.active_player == 1:
        active_player = 1
    else:
        active_player = 2
    counter = 0
    first_row = 0
    first_col = 0
    ai_row = 0
    ai_col = 0

    while len(temp_game.remaining_moves()) > 0:

        if players[active_player - 1] == "Computer":
            ai_row, ai_col = computer_move(temp_game)
            temp_game.assign_move(ai_row, ai_col)
            active_player = temp_game.change_player()
        if counter == 0:
            first_row, first_col = ai_row, ai_col
        counter += 1

    temp_game.determine_winner()
    weighted_score = assign_result_value(temp_game.result)
    return weighted_score, first_row, first_col


def get_best_move(current_board, sim_num):
    temp_game = deepcopy(current_board)
    best_score = 0
    best_row = 0
    best_col = 0
    players = ["Computer", "Computer"]

    for x in range(1, sim_num):
        returned_score, first_row, first_col = sim_game_loop(temp_game, players)
        if returned_score > best_score:
            best_score = returned_score
            best_row = first_row
            best_col = first_col

    return best_row, best_col
