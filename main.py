from graphics import game_loop
import pygame

pygame.init()

display_data = pygame.display.Info()
screen_width, screen_height = (display_data.current_w, display_data.current_h)
board_size = min(screen_width, screen_height)
surface = pygame.display.set_mode((screen_width, screen_height),
                                  pygame.FULLSCREEN)
screen_display = pygame.display
screen_display.set_caption("Mǽrstánas_python")

text_color = "white"
color_light = "ivory4"
display_font = "NotoSans-Regular.ttf"
title_font = pygame.font.Font(display_font, (round(board_size * .035)))
text_font = pygame.font.Font(display_font, (round(board_size * .025)))

game_title = title_font.render("Mǽrstánas", True, text_color)
offset = int(round((board_size / 100) - 2))
top_pos = int(round(board_size * .1))
b_width = int(round((board_size / offset) * 3))
b_height = int(round(b_width / 5))
b_left_pos = int(round((board_size / 2) - (b_width / 2)))

options = dict(option1=["Human vs Computer", int(top_pos + (b_height * 2))],
               option2=["Computer vs Human", int(top_pos + (b_height * 3))],
               option3=["Human vs Human", int(top_pos + (b_height * 4))],
               option4=["Computer vs Computer", int(top_pos + (b_height * 5))],
               option5=["Quit Game", int(top_pos + (b_height * 6))],
               )
text_surfaces = {}

for key in options:
    text = options[key][0]
    text_surfaces[key] = text_font.render(text, True, text_color)


def check_hover_status():
    for i in options:
        if b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
                and options[i][1] <= mouse[1] <= options[i][1] + b_height:
            pygame.draw.rect(
                surface,
                color_light,
                [b_left_pos, options[i][1], b_width, b_height]
            )


def determine_action():
    for i in options:
        if b_left_pos <= mouse[0] <= (b_left_pos + b_width) \
                and options[i][1] <= mouse[1] <= options[i][1] + b_height:
            choice = options[i][0]
            if choice == "Quit Game":
                pygame.quit()
            else:
                words = choice.split(' vs ')
                game_loop(players=(words[0], words[1]))


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
        for key in text_surfaces:
            surface.blit(text_surfaces[key],
                         (b_left_pos + offset, options[key][1] + offset))
        pygame.display.update()
