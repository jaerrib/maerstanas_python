from app.board import Board
from app.game_logic import remaining_moves


class Game:

    def __init__(self):
        self.board = Board()
        self.move_list = []
        self.moves_left = remaining_moves(self.board.data)
        self.score_p1 = 0
        self.score_p2 = 0
        self.result = ""
        self.active_player = 1
        self.active_stone = 1
        self.stone = (self.active_player, self.active_stone)
        self.scoring_type = 1
        self.ruleset = "0.4"
        self.special_stones = {
            "player1": [1, 2, 3],
            "player2": [1, 2, 3],
        }

    def __getitem__(self, key):
        return self.__dict__[key]
