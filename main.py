from graphics import game_loop
import pygame

pygame.init()
res = (900, 900)
surface = pygame.display.set_mode(res)
screen_display = pygame.display
screen_display.set_caption('Mǽrstánas_python')

text_color = "white"
color_light = "ivory4"

# stores the width and height of the screen into a variable
width = surface.get_width()
height = surface.get_height()

# defines the font to be used
text_font = pygame.font.Font('NotoSans-Regular.ttf', (round(width * .025)))

# rendering a text written in this font
game_title = text_font.render('Mǽrstánas', True, text_color)
one_player_first = text_font.render('1 player (first)', True, text_color)
one_player_second = text_font.render('1 player (second)', True, text_color)
two_player = text_font.render('2 player game', True, text_color)
quit_text = text_font.render('quit', True, text_color)
offset = 7

# defining button size
b_width = (width / 7) * 2
b_height = 40

# defining button positions
b_left_pos = (width / 2) - (b_width / 2)
title_pos = 170
b1_y_pos = title_pos + (b_height * 2)
b2_y_pos = title_pos + (b_height * 4)
b3_y_pos = title_pos + (b_height * 6)
b4_y_pos = title_pos + (b_height * 8)

# define game options
player_type = ["Human", "Computer"]
color_choice = ["Brown", "Monochrome"]
color_schemes = {
    "Brown": ["tan", "tan4", "red", "blue"],
    "Monochrome": ["ivory3", "ivory4", "black", "white"],
}
colors = color_schemes[color_choice[1]]


def check_hover_status():
    # if mouse is hovered on a button it changes to lighter shade
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
    """
    Determines action to take based on mouse position
    """
    
    if b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b1_y_pos <= mouse[1] <= (b1_y_pos + b_height):
        game_loop(colors, ["Human", "Computer"])
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b2_y_pos <= mouse[1] <= (b2_y_pos + b_height):
        game_loop(colors, ["Computer", "Human"])
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b3_y_pos <= mouse[1] <= (b3_y_pos + b_height):
        game_loop(colors, ["Human", "Human"])
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b4_y_pos <= mouse[1] <= (b4_y_pos + b_height):
        pygame.quit()
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and title_pos <= mouse[1] <= (title_pos + b_height):
        game_loop(colors, ["Computer", "Computer"])


while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONUP:
            determine_action()

        surface.fill("black")

        # stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos()

        check_hover_status()

        # superimposing the text onto our button
        surface.blit(game_title, (b_left_pos+offset, title_pos+offset))
        surface.blit(one_player_first, (b_left_pos+offset, b1_y_pos+offset))
        surface.blit(one_player_second, (b_left_pos+offset, b2_y_pos+offset))
        surface.blit(two_player, (b_left_pos+offset, b3_y_pos+offset))
        surface.blit(quit_text, (b_left_pos+offset, b4_y_pos+offset))

        # updates the frames of the game
        pygame.display.update()
