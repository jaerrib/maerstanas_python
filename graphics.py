import pygame
from board import Board
from numpy import trunc
from game_logic import valid_move, determine_winner, change_player, \
    computer_move, remaining_moves

pygame.init()

display_data = pygame.display.Info()
screen_width, screen_height = (display_data.current_w, display_data.current_h)
board_width, board_height = (screen_height, screen_height)

surface = pygame.display.set_mode((screen_width,screen_height),
                                  pygame.FULLSCREEN)

stone_click = pygame.mixer.Sound("sound/stone.ogg")
win = pygame.mixer.Sound("sound/win.ogg")
lose = pygame.mixer.Sound("sound/lose.ogg")
tie = pygame.mixer.Sound("sound/tie.ogg")

cell_size = int(round(board_height / 7))
cell_modifier = int(round(cell_size * .1))

stone_size = int(round(cell_size * .80))
stone_dimensions = (stone_size, stone_size)

dark_stone = pygame.image.load("images/dark_stone.svg")
dark_stone = pygame.transform.smoothscale(dark_stone, stone_dimensions)
light_stone = pygame.image.load("images/light_stone.svg")
light_stone = pygame.transform.smoothscale(light_stone, stone_dimensions)
board_img = pygame.image.load("images/board.svg")
board_img = pygame.transform.smoothscale(board_img, (board_width, board_height))

offset = int(round((board_width / 100) - 2))
b_width = int(round(board_width / 2))
b_height = int(round(((board_width / offset) * 2) / 5))


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
    text_font = pygame.font.Font('NotoSans-Regular.ttf',
                                 (round(board_width * .025)))
    p1_score_txt = text_font.render(
        f"Player 1 ({player1}) score: {score_p1}",
        True,
        text_color
    )
    p2_score_txt = text_font.render(
        f"Player 2 ({player2}) score: {score_p2}",
        True,
        text_color
    )
    result_txt = ""
    if winner == "tie":
        result_txt = text_font.render(
            "It's a tie!",
            True,
            text_color
        )
    elif winner == "player 1":
        result_txt = text_font.render(
            f"Player 1 wins!",
            True,
            text_color
        )
    elif winner == "player2":
        result_txt = text_font.render(
            f"Player 2 wins!",
            True,
            text_color
        )
    continue_text = text_font.render(
        "Click to continue",
        True,
        text_color
    )

    b_left_pos = int(round((board_width / 2) - (b_width / 2)))
    top_pos = int(round(board_width * .1))
    b1_y_pos = int(top_pos + (b_height * 2))
    b2_y_pos = int(top_pos + (b_height * 4))
    b3_y_pos = int(top_pos + (b_height * 6))

    box_color = "black"

    pygame.draw.rect(
        surface,
        box_color,
        [b_left_pos, top_pos, b_width, b_height]
    )
    pygame.draw.rect(
        surface,
        box_color,
        [b_left_pos, b1_y_pos, b_width, b_height]
    )
    pygame.draw.rect(
        surface,
        box_color,
        [b_left_pos, b2_y_pos, b_width, b_height]
    )
    pygame.draw.rect(
        surface,
        box_color,
        [b_left_pos, b3_y_pos, b_width, b_height]
    )

    play_game_over_sound(winner, player1, player2)

    surface.blit(p1_score_txt, (b_left_pos + offset, top_pos + offset))
    surface.blit(p2_score_txt, (b_left_pos + offset, b1_y_pos + offset))
    surface.blit(result_txt, (b_left_pos + offset, b2_y_pos + offset))
    surface.blit(continue_text, (b_left_pos + offset, b3_y_pos + offset))
    pygame.display.flip()


def draw_stone(color, x_pos, y_pos):

    print(x_pos, y_pos)


    if color == "black":
        surface.blit(dark_stone, (x_pos, y_pos))
    if color == "white":
        surface.blit(light_stone, (x_pos, y_pos))
    pygame.display.flip()


def game_loop(color_scheme, players):
    board = Board()
    active_player = 1
    player1 = players[0]
    player2 = players[1]
    surface.blit(board_img, (0,0))
    colors = [color_scheme[2], color_scheme[3]]
    running = True

    while running:
        for event in pygame.event.get():
            active_color = colors[active_player - 1]

            if players[active_player - 1] == "Computer":
                pygame.time.wait(500)
                if len(remaining_moves(board.data)) < 1:
                    running = False
                else:
                    ai_row, ai_col = computer_move(board.data,
                                                   active_player)

                    x_draw = ((ai_col - 1) * cell_size) + cell_modifier
                    y_draw = ((ai_row - 1) * cell_size) + cell_modifier
                    draw_stone(active_color,x_draw,y_draw)
                    active_player = change_player(active_player)
                    pygame.mixer.Sound.play(stone_click)

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP and \
                    players[active_player - 1] == "Human":
                x, y = pygame.mouse.get_pos()
                converted_pos = convert_pos(x, y)
                if valid_move(board.data,
                              converted_pos[3],
                              converted_pos[2],
                              active_player):
                    draw_stone(active_color,
                               converted_pos[0],
                               converted_pos[1])
                    active_player = change_player(active_player)
                    pygame.mixer.Sound.play(stone_click)
                    pygame.time.wait(250)
            if len(remaining_moves(board.data)) < 1:
                running = False
            pygame.display.flip()

    winner, score_p1, score_p2 = determine_winner(board.data)
    display_game_results(winner, score_p1, score_p2, player1, player2)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.MOUSEBUTTONUP:
                waiting = False
