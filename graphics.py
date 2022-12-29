import pygame
from board import Board
from numpy import trunc
from game_logic import valid_move, determine_winner, change_player, \
    computer_move, remaining_moves

pygame.init()

# Gets display dimensions then sets the board size and surface variables
display_data = pygame.display.Info()
screen_width, screen_height = (display_data.current_w, display_data.current_h)
width, height = (screen_height, screen_height)

surface = pygame.display.set_mode((screen_width,screen_height),
                                  pygame.FULLSCREEN)

stone_click = pygame.mixer.Sound("sound/stone.ogg")
win = pygame.mixer.Sound("sound/win.ogg")
lose = pygame.mixer.Sound("sound/lose.ogg")
tie = pygame.mixer.Sound("sound/tie.ogg")

offset = int(round((width / 100) - 2))
b_width = int(round(width / 2))
b_height = int(round(((width / offset) * 2) / 5))

def draw_board(color_scheme):
    light_color = color_scheme[0]
    dark_color = color_scheme[1]
    cell_size = height / 7

    for y_pos in range(7):
        y = y_pos * cell_size
        if y_pos % 2 == 0:
            color1 = light_color
            color2 = dark_color
        else:
            color1 = dark_color
            color2 = light_color
        for x_pos in range(7):
            x = x_pos * cell_size
            if x_pos % 2 == 0:
                pygame.draw.rect(surface, color1,
                                 pygame.Rect(x, y, cell_size, cell_size))
            elif x_pos % 2 != 0:
                pygame.draw.rect(surface, color2,
                                 pygame.Rect(x, y, cell_size, cell_size))
    pygame.display.flip()


def convert_pos(col, row):
    cell_size = height / 7
    cell_modifier = cell_size / 2
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
    text_font = pygame.font.Font('NotoSans-Regular.ttf', (round(width * .025)))
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

    b_left_pos = int(round((width / 2) - (b_width / 2)))
    top_pos = int(round(width * .1))
    b1_y_pos = int(top_pos + (b_height * 2))
    b2_y_pos = int(top_pos + (b_height * 4))
    b3_y_pos = int(top_pos + (b_height * 6))

    # drawing transparent rectangles to make text easier to see
    box_color = (0, 0, 0, 128)

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

    # superimposing the text onto our button
    surface.blit(p1_score_txt, (b_left_pos + offset, top_pos + offset))
    surface.blit(p2_score_txt, (b_left_pos + offset, b1_y_pos + offset))
    surface.blit(result_txt, (b_left_pos + offset, b2_y_pos + offset))
    surface.blit(continue_text, (b_left_pos + offset, b3_y_pos + offset))
    pygame.display.flip()


def draw_stone(color, x_pos, y_pos):
    stone_size = int(round(height * .05))
    border = int(round(stone_size * .15))
    pygame.draw.circle(surface,
                       color,
                       (x_pos, y_pos),
                       stone_size)
    pygame.draw.circle(surface,
                       pygame.Color(32, 32, 32, a=32),
                       (x_pos, y_pos),
                       stone_size,
                       width=border)
    pygame.display.flip()


def game_loop(color_scheme, players):
    board = Board()
    active_player = 1
    player1 = players[0]
    player2 = players[1]
    surface.fill("black")
    draw_board(color_scheme)
    colors = [color_scheme[2], color_scheme[3]]
    running = True

    while running:
        for event in pygame.event.get():
            active_color = colors[active_player - 1]
            # if active player is computer then make computer move and
            # change players
            if players[active_player - 1] == "Computer":
                if len(remaining_moves(board.data)) < 1:
                    running = False
                else:
                    ai_row, ai_col = computer_move(board.data,
                                                   active_player)
                    x, y = surface.get_size()
                    cell_size = y / 7
                    cell_modifier = cell_size / 2

                    x_draw = ((ai_col - 1) * cell_size) + cell_modifier
                    y_draw = ((ai_row - 1) * cell_size) + cell_modifier
                    draw_stone(active_color,x_draw,y_draw)
                    active_player = change_player(active_player)
                    pygame.mixer.Sound.play(stone_click)
                    pygame.time.wait(1000)

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
                    pygame.time.wait(1000)
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
