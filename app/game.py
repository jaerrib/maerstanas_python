from app.board import Board
from app.game_logic import remaining_moves


class Game:

    def __init__(self, size):
        self.board = Board(size)
        self.move_list = []
        self.moves_left = remaining_moves(self.board.data)
        self.score_p1 = 0
        self.score_p2 = 0
        self.result = ""
        self.active_player = 1
        self.scoring_type = 1
