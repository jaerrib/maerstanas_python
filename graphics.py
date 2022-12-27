import pygame
from board import Board
from numpy import trunc
from game_logic import valid_move, determine_winner, change_player, \
    computer_move, remaining_moves

pygame.init()
surface = pygame.display.set_mode((900, 900))
stone_click = pygame.mixer.Sound("click.wav")

def draw_board(color_scheme):
    light_color = color_scheme[0]
    dark_color = color_scheme[1]
    x, y = surface.get_size()
    cell_size = y / 7
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
    """
    Test code to see if positions can be variable based on screen size
    x, y = surface.get_size()
    """
    x, y = surface.get_size()
    cell_size = y / 7
    cell_modifier = cell_size / 2
    row_pos = int(trunc(row / cell_size))
    col_pos = int(trunc(col / cell_size))
    x_index = col_pos + 1
    y_index = row_pos + 1
    x_draw = (col_pos * cell_size) + cell_modifier
    y_draw = (row_pos * cell_size) + cell_modifier
    return x_draw, y_draw, x_index, y_index


def display_game_results(winner, score_p1, score_p2, player1, player2):
    # stores the width of the screen into a variable
    width = surface.get_width()
    text_color = "white"
    # defines text area size based on width of screen
    b_width = round(width / 2)
    b_height = 40
    offset = 7

    smallfont = pygame.font.Font('NotoSans-Regular.ttf', (round(width * .025)))
    p1_score_txt = smallfont.render(
        f"Player 1 ({player1}) score: {score_p1}",
        True,
        text_color
    )
    p2_score_txt = smallfont.render(
        f"Player 2 ({player2}) score: {score_p2}",
        True,
        text_color
    )
    result_txt = ""
    if winner == "tie":
        result_txt = smallfont.render(
            "It's a tie!",
            True,
            text_color
        )
    elif winner == "player 1":
        result_txt = smallfont.render(
            f"Player 1 wins!",
            True,
            text_color
        )
    elif winner == "player2":
        result_txt = smallfont.render(
            f"Player 2 wins!",
            True,
            text_color
        )
    continue_text = smallfont.render(
        "Click to continue",
        True,
        text_color
    )

    b_left_pos = width / 4
    title_pos = 170
    b1_y_pos = title_pos + (b_height * 2)
    b2_y_pos = title_pos + (b_height * 4)
    b3_y_pos = title_pos + (b_height * 6)

    # drawing transparent rectangles to make text easier to see
    box_color = (0, 0, 0, 128)

    pygame.draw.rect(
        surface,
        box_color,
        [b_left_pos, title_pos, b_width, b_height]
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

    # superimposing the text onto our button
    surface.blit(p1_score_txt, (b_left_pos + offset, title_pos + offset))
    surface.blit(p2_score_txt, (b_left_pos + offset, b1_y_pos + offset))
    surface.blit(result_txt, (b_left_pos + offset, b2_y_pos + offset))
    surface.blit(continue_text, (b_left_pos + offset, b3_y_pos + offset))
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
                    pygame.draw.circle(surface,
                                       active_color,
                                       (x_draw, y_draw),
                                       35)
                    pygame.draw.circle(surface,
                                       pygame.Color(32, 32, 32, a=32),
                                       (x_draw, y_draw),
                                       35,
                                       width=5)
                    active_player = change_player(active_player)
                    pygame.display.flip()
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
                    pygame.draw.circle(surface,
                                       active_color,
                                       (converted_pos[0],
                                        converted_pos[1]),
                                       35)
                    pygame.draw.circle(surface,
                                       pygame.Color(32, 32, 32, a=32),
                                       (converted_pos[0],
                                        converted_pos[1]),
                                       35,
                                       width=5)
                    active_player = change_player(active_player)
                    pygame.display.flip()
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
