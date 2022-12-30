from graphics import game_loop
import pygame

pygame.init()

display_data = pygame.display.Info()
screen_width, screen_height = (display_data.current_w, display_data.current_h)
board_size = min(screen_width, screen_height)
surface = pygame.display.set_mode((screen_width,screen_height),
                                  pygame.FULLSCREEN)
screen_display = pygame.display
screen_display.set_caption('Mǽrstánas_python')

text_color = "white"
color_light = "ivory4"
title_font = pygame.font.Font('NotoSans-Regular.ttf', (round(board_size * .035)))
text_font = pygame.font.Font('NotoSans-Regular.ttf', (round(board_size * .025)))

game_title = title_font.render('Mǽrstánas', True, text_color)
one_player_first = text_font.render('1 player (first)', True, text_color)
one_player_second = text_font.render('1 player (second)', True, text_color)
two_player = text_font.render('2 player game', True, text_color)
quit_text = text_font.render('quit', True, text_color)
offset = int(round((board_size / 100) - 2))

b_width = int(round((board_size / offset) * 2))
b_height = int(round(b_width / 5))

b_left_pos = int(round((board_size / 2) - (b_width / 2)))
top_pos = int(round(board_size * .1))
b1_y_pos = int(top_pos + (b_height * 2))
b2_y_pos = int(top_pos + (b_height * 3))
b3_y_pos = int(top_pos + (b_height * 4))
b4_y_pos = int(top_pos + (b_height * 5))


def check_hover_status():
    if b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b1_y_pos <= mouse[1] <= (b1_y_pos + b_height):
        pygame.draw.rect(
            surface,
            color_light,
            [b_left_pos, b1_y_pos, b_width, b_height]
        )
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b2_y_pos <= mouse[1] <= (b2_y_pos + b_height):
        pygame.draw.rect(
            surface,
            color_light,
            [b_left_pos, b2_y_pos, b_width, b_height]
        )
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b3_y_pos <= mouse[1] <= (b3_y_pos + b_height):
        pygame.draw.rect(
            surface,
            color_light,
            [b_left_pos, b3_y_pos, b_width, b_height]
        )
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b4_y_pos <= mouse[1] <= (b4_y_pos + b_height):
        pygame.draw.rect(
            surface,
            color_light,
            [b_left_pos, b4_y_pos, b_width, b_height]
        )


def determine_action():

    if b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b1_y_pos <= mouse[1] <= (b1_y_pos + b_height):
        game_loop(["Human", "Computer"])
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b2_y_pos <= mouse[1] <= (b2_y_pos + b_height):
        game_loop(["Computer", "Human"])
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b3_y_pos <= mouse[1] <= (b3_y_pos + b_height):
        game_loop(["Human", "Human"])
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b4_y_pos <= mouse[1] <= (b4_y_pos + b_height):
        pygame.quit()
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and top_pos <= mouse[1] <= (top_pos + b_height):
        game_loop(["Computer", "Computer"])


while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONUP:
            determine_action()
        surface.fill("black")
        mouse = pygame.mouse.get_pos()
        check_hover_status()
        surface.blit(game_title, (b_left_pos + offset, top_pos + offset))
        surface.blit(one_player_first, (b_left_pos+offset, b1_y_pos+offset))
        surface.blit(one_player_second, (b_left_pos+offset, b2_y_pos+offset))
        surface.blit(two_player, (b_left_pos+offset, b3_y_pos+offset))
        surface.blit(quit_text, (b_left_pos+offset, b4_y_pos+offset))
        pygame.display.update()
