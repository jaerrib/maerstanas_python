from copy import deepcopy
import secrets

player_list = ["Computer", "Computer"]


def assign_result_value(current_game):
    game_value = 0
    score_p1 = current_game.check_score(1)
    score_p2 = current_game.check_score(2)
    if current_game.result == "tie":
        game_value = 1
    elif current_game.result == "player 1":
        game_value = 4
    elif current_game.result == "player 2":
        game_value = -2
    difference = abs(score_p1 - score_p2)
    game_value = game_value * difference
    return game_value


def computer_move(current_game):
    comp_move = secrets.choice(current_game.remaining_moves())
    row, col = comp_move[0], comp_move[1]
    return row, col


def sim_game_loop(current_board, players, depth):
    temp_game = deepcopy(current_board)
    comparison_player = deepcopy(temp_game.active_player)
    if temp_game.active_player == 1:
        active_player = 1
    else:
        active_player = 2
    first_row = 0
    first_col = 0
    first_move = True
    depth_counter = min(depth, len(temp_game.remaining_moves()))

    while depth_counter >= 1:
        if players[active_player - 1] == "Computer":
            if len(temp_game.remaining_moves()) >= 1:
                ai_row, ai_col = computer_move(temp_game)
                if first_move:
                    first_row = ai_row
                    first_col = ai_col
                    first_move = False
                temp_game.assign_move(ai_row, ai_col)
                temp_game.update_score()
                active_player = temp_game.change_player()
        depth_counter -= 1

    temp_game.determine_winner()
    if comparison_player == 1:
        weighted_score = assign_result_value(temp_game)
    else:
        weighted_score = -(assign_result_value(temp_game))
    return weighted_score, first_row, first_col


def get_best_move(current_board, sim_num, depth):
    temp_game = deepcopy(current_board)
    best_score = 0
    best_row = 0
    best_col = 0
    players = ["Computer", "Computer"]

    for x in range(0, sim_num):
        returned_score, first_row, first_col = sim_game_loop(temp_game,
                                                             players,
                                                             depth)
        if x == 1:
            best_score = returned_score
            best_row = first_row
            best_col = first_col
        if returned_score > best_score:
            best_score = returned_score
            best_row = first_row
            best_col = first_col
    return best_row, best_col
