from board import Board

class Game:

    def __init__(self):
        self.board = Board()
        self.move_list = {}
        self.moves_left = []
        self.score_p1 = 0
        self.score_p2 = 0
        self.result = ""
        self.active_player = 1