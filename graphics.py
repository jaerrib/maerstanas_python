import pygame
from game import Game
from numpy import trunc
from ai_player import get_best_move
from pygame import mixer

pygame.init()
mixer.init()
invalid_move = mixer.Sound("sound/invalid.ogg")

display_data = pygame.display.Info()
screen_width, screen_height = (display_data.current_w, display_data.current_h)
board_size = min(screen_width, screen_height) * .9

surface = pygame.display.set_mode((screen_width, screen_height),
                                  pygame.FULLSCREEN)

stone_click = pygame.mixer.Sound("sound/stone.ogg")
win = pygame.mixer.Sound("sound/win.ogg")
lose = pygame.mixer.Sound("sound/lose.ogg")
tie = pygame.mixer.Sound("sound/tie.ogg")

cell_size = int(round(board_size / 7))
cell_modifier = int(round(cell_size * .1))

stone_size = int(round(cell_size * .80))
stone_dimensions = (stone_size, stone_size)

offset = int(round((board_size / 100) - 2))
top_pos = int(round(board_size * .1))
b_width = int(round(board_size / 2))
b_height = int(round(((board_size / offset) * 2) / 5))
b_left_pos = int(round((board_size / 2) - (b_width / 2)))


def convert_pos(col, row):
    row_pos = int(trunc(row / cell_size))
    col_pos = int(trunc(col / cell_size))
    x_index = col_pos + 1
    y_index = row_pos + 1
    x_draw = (col_pos * cell_size) + cell_modifier
    y_draw = (row_pos * cell_size) + cell_modifier
    return x_draw, y_draw, x_index, y_index


def play_game_over_sound(winner, player1, player2):
    if winner == "tie":
        pygame.mixer.Sound.play(tie)
    elif player1 == player2:
        pygame.mixer.Sound.play(win)
    elif player1 == "Computer" and winner == "player 1":
        pygame.mixer.Sound.play(lose)
    elif player2 == "Computer" and winner == "player 2":
        pygame.mixer.Sound.play(lose)
    else:
        pygame.mixer.Sound.play(win)


def display_game_results(winner, score_p1, score_p2, player1, player2):
    text_color = "white"
    box_color = "black"
    text_font = pygame.font.Font('NotoSans-Regular.ttf',
                                 (round(board_size * .025)))
    if winner == "tie":
        result_txt = "It's a tie!"
    else:
        result_txt = winner.capitalize()+" wins!"

    results_dict = dict(line1=["Player 1 ("+player1+") score: "+str(score_p1),
                               top_pos],
                        line2=["Player 2 ("+player2+") score: "+str(score_p2),
                               int(top_pos + (b_height * 2))],
                        line3=[result_txt,
                               int(top_pos + (b_height * 4))],
                        line4=["Click to continue",
                               int(top_pos + (b_height * 6))],
                        )
    text_surfaces = {}

    for key in results_dict:
        text = results_dict[key][0]
        text_surfaces[key] = text_font.render(text, True, text_color)

    for i in results_dict:
        pygame.draw.rect(
            surface,
            box_color,
            [b_left_pos, results_dict[i][1], b_width, b_height]
            )

    for j in text_surfaces:
        surface.blit(text_surfaces[j],
                     (b_left_pos + offset, results_dict[j][1] + offset))

    play_game_over_sound(winner, player1, player2)
    pygame.display.flip()


def draw_stones(game):
    colors = ["dark", "light"]
    length = len(game.move_list)
    stones = {}
    for i in range(0, length):
        key = str(i)
        if i%2 == 0:
            active_color = colors[0]
        else:
            active_color = colors[1]
        if i == length - 1:
            stones[key] = pygame.image.load(
                "images/last_played_" + active_color + ".svg")
        else:
            stones[key] = pygame.image.load("images/"+active_color+"_stone.svg")
        stones[key] = pygame.transform.smoothscale(stones[key],
                                                   stone_dimensions)
        col_pos = game.move_list[key][1] - 1
        row_pos = game.move_list[key][0] - 1
        x_draw = (col_pos * cell_size) + cell_modifier
        y_draw = (row_pos * cell_size) + cell_modifier
        surface.blit(stones[key], (x_draw, y_draw))
    pygame.display.flip()


def display_score(board, players):
    player1 = players[0]
    player2 = players[1]
    board.update_score()
    text_color = "white"
    box_color = "black"
    vert_pos = board_size + offset
    p1_score_pos = offset
    p2_score_pos = (board_size / 2) + offset
    text_font = pygame.font.Font('NotoSans-Regular.ttf',
                                 (round(board_size * .025)))

    score_dict = dict(
        p1=["Player 1 ("+player1+") score: "+str(board.score_p1), p1_score_pos],
        p2=["Player 2 ("+player2+") score: "+str(board.score_p2), p2_score_pos],
    )

    text_surfaces = {}
    for key in score_dict:
        text = score_dict[key][0]
        text_surfaces[key] = text_font.render(text, True, text_color, box_color)

    for j in text_surfaces:
        surface.blit(text_surfaces[j],
                     (score_dict[j][1], vert_pos))
    pygame.display.flip()


def game_loop(players):
    game = Game()
    active_player = game.active_player
    player1 = players[0]
    player2 = players[1]
    board_img = pygame.image.load("images/board.svg")
    board_img = pygame.transform.smoothscale(board_img,
                                             (board_size, board_size))
    surface.blit(board_img, (0, 0))
    running = True

    while running:
        if players[active_player - 1] == "Computer":
            pygame.time.wait(500)
            if len(game.remaining_moves()) < 1:
                running = False
            else:
                ai_row, ai_col = get_best_move(game, 100, 49)
                game.assign_move(ai_row, ai_col)
                draw_stones(game)
                active_player = game.change_player()
                pygame.mixer.Sound.play(stone_click)
        if players[active_player - 1] == "Human":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    converted_pos = convert_pos(x, y)
                    if game.valid_move(converted_pos[3], converted_pos[2]):
                        game.assign_move(converted_pos[3], converted_pos[2])
                        draw_stones(game)
                        active_player = game.change_player()
                        pygame.mixer.Sound.play(stone_click)
                        # pygame.time.wait(250)
                    else:
                        mixer.Sound.play(invalid_move)
            if len(game.remaining_moves()) < 1:
                running = False
            display_score(game, players)
            pygame.display.flip()

    game.update_score()
    game.determine_winner()
    display_game_results(game.result,
                         game.score_p1,
                         game.score_p2,
                         player1,
                         player2)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.MOUSEBUTTONUP:
                waiting = False
