from board import Board
from game_logic import remaining_moves, assign_move, change_player, determine_winner, computer_move
from copy import copy

player_list = ["Computer", "Computer"]
simulations = 10
depth = 3


def assign_result_value(result):
    if result == "tie":
        return 1
    elif result == "player 1":
        return 2
    elif result == "player 2":
        return -2


def sim_game_loop(current_board, players):
    temp_board = Board()
    temp_board.data = copy(current_board.data)
    temp_board.move_list = copy(current_board.move_list)
    active_player = 2
    # player1 = players[0]
    # player2 = players[1]
    counter = 0
    first_row = 0
    first_col = 0
    ai_row = 0
    ai_col = 0

    while len(remaining_moves(temp_board.data)) > 0:

        if players[active_player - 1] == "Computer":
            ai_row, ai_col = computer_move(temp_board.data)
            assign_move(temp_board, ai_row, ai_col, active_player)
            active_player = change_player(active_player)
        if counter == 0:
            first_row, first_col = ai_row, ai_col
        counter += 1

    result, score_p1, score_p2 = determine_winner(temp_board.data)
    weighted_score = assign_result_value(result)
    return weighted_score, first_row, first_col


def get_best_move(current_board, sim_num):
    temp_board = Board()
    temp_board.data = copy(current_board.data)
    temp_board.move_list = copy(current_board.move_list)
    best_score = 0
    best_row = 0
    best_col = 0
    players = ["Computer", "Computer"]

    for x in range(sim_num):
        returned_score, first_row, first_col = sim_game_loop(temp_board, players)
        if returned_score > best_score:
            best_score = returned_score
            best_row = first_row
            best_col = first_col

    return best_row, best_col


# board = Board()
# print(get_best_move(board, simulations))