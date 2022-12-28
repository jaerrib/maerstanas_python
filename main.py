from graphics import game_loop
import pygame

pygame.init()

# Gets display dimensions then sets the board size and surface variables
display_data = pygame.display.Info()
screen_width, screen_height = (display_data.current_w, display_data.current_h)
width, height = (screen_height, screen_height)

surface = pygame.display.set_mode((screen_width,screen_height),
                                  pygame.FULLSCREEN)
screen_display = pygame.display
screen_display.set_caption('Mǽrstánas_python')

text_color = "white"
color_light = "ivory4"

# Defines the font to be used
text_font = pygame.font.Font('NotoSans-Regular.ttf', (round(width * .025)))

# Rendering the text
game_title = text_font.render('Mǽrstánas', True, text_color)
one_player_first = text_font.render('1 player (first)', True, text_color)
one_player_second = text_font.render('1 player (second)', True, text_color)
two_player = text_font.render('2 player game', True, text_color)
quit_text = text_font.render('quit', True, text_color)
offset = int(round((width / 100) - 2))

# defining button size
b_width = int(round((width / offset) * 2))
b_height = int(round(b_width / 5))

# defining button positions
b_left_pos = int(round((width / 2) - (b_width / 2)))
top_pos = int(round(width * .1))
b1_y_pos = int(top_pos + (b_height * 2))
b2_y_pos = int(top_pos + (b_height * 3))
b3_y_pos = int(top_pos + (b_height * 4))
b4_y_pos = int(top_pos + (b_height * 5))

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
            and top_pos <= mouse[1] <= (top_pos + b_height):
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
        surface.blit(game_title, (b_left_pos + offset, top_pos + offset))
        surface.blit(one_player_first, (b_left_pos+offset, b1_y_pos+offset))
        surface.blit(one_player_second, (b_left_pos+offset, b2_y_pos+offset))
        surface.blit(two_player, (b_left_pos+offset, b3_y_pos+offset))
        surface.blit(quit_text, (b_left_pos+offset, b4_y_pos+offset))

        # updates the frames of the game
        pygame.display.update()
