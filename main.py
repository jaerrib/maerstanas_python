import sys
from game_logic import *
from settings import *


def main_loop():
    continue_play = True
    while continue_play:
        system('clear')
        players = get_players()
        play_game(players)
        play_again = input("Play a new game (y/n)?").lower()
        continue_play = play_again == "y"


main_loop()
sys.exit()
