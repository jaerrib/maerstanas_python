def get_players():
    players = ["computer", "computer"]

    def play_as(player_list):
        human_player = int(input("Would you like to be player 1 or 2?"))
        if human_player == 1 or human_player == 2:
            player_list[human_player - 1] = "human"
        else:
            play_as(player_list)
        return player_list

    def number_of_players(player_list):
        # Uncomment the next line to test 2 computer players
        # return players
        number_players = int(input("1 or 2 player game? "))
        if number_players == 2:
            player_list = ["human", "human"]
        elif number_players == 1:
            play_as(player_list)
        else:
            number_of_players(player_list)
        return player_list

    number_of_players(players)
    return players


def get_colors():
    color_schemes = {
        "Brown": ["tan", "tan4", "black", "white"],
        "Monochrome": ["ivory3", "ivory4", "black", "white"],
    }
    for setting in color_schemes:
        print(color_schemes[setting])
    choice = input("Choose a color setting: ")
    return choice
