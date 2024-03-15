import secrets
from copy import deepcopy

from app.game_logic import (
    assign_move,
    determine_winner,
    check_score,
    possible_thunder_stone_moves,
    possible_woden_stone_moves,
    is_game_over,
    player_must_pass,
    change_player,
)


def assign_result_value(current_game):
    game_value = 0
    score_p1 = check_score(
        board=current_game["board"], score_type=current_game["scoring_type"], player=1
    )
    score_p2 = check_score(
        board=current_game["board"], score_type=current_game["scoring_type"], player=2
    )
    if current_game["result"] == "tie":
        game_value = 1
    elif current_game["result"] == "player 1":
        game_value = 4
    elif current_game["result"] == "player 2":
        game_value = -2
    difference = abs(score_p1 - score_p2)
    adjustment = 48 - len(current_game["move_list"])
    game_value = game_value * difference * adjustment
    return game_value


def get_available_moves(temp_game):
    active_player = temp_game["active_player"]
    standard_moves = temp_game["moves_left"]
    thunder_moves = []
    woden_moves = []
    if 2 in temp_game["special_stones"]["player" + str(active_player)]:
        thunder_moves.append(possible_thunder_stone_moves(temp_game))
    if 3 in temp_game["special_stones"]["player" + str(active_player)]:
        woden_moves.append(possible_woden_stone_moves(temp_game))
    thunder_moves = [item for sublist in thunder_moves for item in sublist]
    woden_moves = [item for sublist in woden_moves for item in sublist]
    possible_moves = standard_moves + thunder_moves + woden_moves
    moves = {
        "standard": standard_moves,
        "thunder": thunder_moves,
        "woden": woden_moves,
        "possible": possible_moves,
    }
    return moves


def computer_move(temp_game):
    moves = get_available_moves(temp_game)
    comp_move = secrets.choice(moves["possible"])
    row, col = comp_move[0], comp_move[1]
    if (comp_move in moves["thunder"] and len(moves["standard"]) < 12) or (
        comp_move in moves["thunder"] and comp_move not in moves["standard"]
    ):
        stone = 2
    elif comp_move in moves["woden"]:
        stone = 3
    else:
        stone = 1
    return stone, row, col


def sim_game_loop(data, players, depth):
    temp_game = deepcopy(data)
    comparison_player = deepcopy(temp_game["active_player"])
    if temp_game["active_player"] == 1:
        active_player = 1
    else:
        active_player = 2
    first_move = True
    moves = get_available_moves(temp_game)
    depth_counter = min(depth, len(moves["possible"]))
    while depth_counter >= 1:
        if players[active_player - 1] == "Computer":
            if not is_game_over(temp_game) and not player_must_pass(temp_game):
                moves = get_available_moves(temp_game)
                if len(moves["possible"]) >= 1:
                    ai_stone, ai_row, ai_col = computer_move(temp_game)
                if first_move:
                    first_row = ai_row
                    first_col = ai_col
                    first_stone = ai_stone
                    first_move = False
                temp_game = assign_move(temp_game, ai_row, ai_col)
            if player_must_pass(temp_game):
                change_player(temp_game)
        depth_counter -= 1

    temp_game["result"] = determine_winner(temp_game["score_p1"], temp_game["score_p2"])
    if comparison_player == 1:
        weighted_score = assign_result_value(temp_game)
    else:
        weighted_score = -(assign_result_value(temp_game))
    return weighted_score, first_stone, first_row, first_col


def get_best_move(data, sim_num, depth):
    temp_game = deepcopy(data)
    # Using -1000 simply ensures that losses and ties are scored
    # better than the initial assignment
    best_score = -1000
    players = ["Computer", "Computer"]

    for x in range(0, sim_num):
        returned_score, first_stone, first_row, first_col = sim_game_loop(
            temp_game, players, depth
        )
        if returned_score >= best_score:
            best_score = returned_score
            best_row = first_row
            best_col = first_col
            best_stone = first_stone
    return best_stone, best_row, best_col
