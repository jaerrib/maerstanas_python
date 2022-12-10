from graphics import gui_loop_test2
import pygame

# import sys

# initializing the constructor
pygame.init()

# screen resolution
res = (900, 900)

# opens up a window
surface = pygame.display.set_mode(res)
screen_display = pygame.display
screen_display.set_caption('Maerstanas_python')

# white color
color = "white"

# light shade of the button
color_light = "ivory4"

# dark shade of the button
color_dark = "ivory4"

# stores the width of the
# screen into a variable
width = surface.get_width()

# stores the height of the
# screen into a variable
height = surface.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', (round(width * .05)))

# rendering a text written in this font
game_title = smallfont.render('Maerstanas', True, color)
one_player_first = smallfont.render('1 player (first)', True, color)
one_player_second = smallfont.render('1 player (second)', True, color)
two_player = smallfont.render('2 player game', True, color)
quit_text = smallfont.render('quit', True, color)
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
    # if mouse is hovered on a button it
    # changes to lighter shade
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
    return


def determine_action():
    # determines action to take based on mouse position
    
    if b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b1_y_pos <= mouse[1] <= (b1_y_pos + b_height):
        # pygame.time.delay(1500)
        gui_loop_test2(colors, ["Human", "Computer"])
        return
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b2_y_pos <= mouse[1] <= (b2_y_pos + b_height):
        gui_loop_test2(colors, ["Computer", "Human"])
        return
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b3_y_pos <= mouse[1] <= (b3_y_pos + b_height):
        gui_loop_test2(colors, ["Human", "Human"])
        return
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and b4_y_pos <= mouse[1] <= (b4_y_pos + b_height):
        pygame.quit()
        return
    elif b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
            and title_pos <= mouse[1] <= (title_pos + b_height):
        gui_loop_test2(colors, ["Computer", "Computer"])
        return
    

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONUP:
            determine_action()

        # fills the screen with a color
        surface.fill("black")

        # stores the (x,y) coordinates into
        # the variable as a tuple
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
