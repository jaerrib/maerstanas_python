import pygame
from numpy import trunc
from game_logic import *
pygame.init()
surface = pygame.display.set_mode((700, 700))


def draw_board(color_scheme):
    light_color = color_scheme[0]
    dark_color = color_scheme[1]
    x, y = surface.get_size()
    cell_size = y / 2
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


def position_round(col, row):
    row_pos = int(trunc(row / 100))
    col_pos = int(trunc(col / 100))
    # index = (y_pos + 1, x_pos + 1)
    # valid_move(index)
    x_draw = (col_pos * 100) + 50
    y_draw = (row_pos * 100) + 50
    return x_draw, y_draw


def gui_loop_test():
    """
    Currently broken placeholder code
    """
    board = create_board()
    players = ["human", "human"]
    active_player = 1
    player1 = players[0]
    player2 = players[1]
    draw_board(color_scheme)

    while viable_moves(board):
        pygame.display.flip()
        score_p1 = check_score(board, 1)
        score_p2 = check_score(board, 2)
        print(f"Player 1 ({player1}) score: {score_p1}")
        print(f"Player 1 ({player2}) score: {score_p2}")
        print()
        if players[active_player - 1] == "human":
            print(f"Player {active_player}'s turn")
            # entered_move = (
            #    input("Enter row and column - with no spaces - to "
            #          "place your stone: ")
            # )
            active_color = ["white", "black"]
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        x, y = pygame.mouse.get_pos()
                        draw_pos = position_round(x, y)
                        if valid_move(board, draw_pos[1], draw_pos[0],
                                      active_player):
                            pygame.draw.circle(surface,
                                               active_color[active_player - 1],
                                               draw_pos, 35)
                            pygame.display.flip()
    determine_winner(board, player1, player2)
    # quit pygame after closing window
    pygame.quit()
