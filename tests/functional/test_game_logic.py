import unittest

from app.game import Game
from app.game_logic import *


class GameLogicTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.board["data"] = [
            [
                (3, 3),
                (3, 3),
                (3, 3),
                (3, 3),
                (3, 3),
                (3, 3),
                (3, 3),
                (3, 3),
                (3, 3),
            ],
            [
                (3, 3),
                (1, 1),
                (1, 1),
                (0, 0),
                (1, 1),
                (2, 1),
                (0, 0),
                (2, 1),
                (3, 3),
            ],
            [
                (3, 3),
                (0, 0),
                (1, 1),
                (1, 1),
                (1, 1),
                (2, 2),
                (2, 2),
                (2, 2),
                (3, 3),
            ],
            [
                (3, 3),
                (0, 0),
                (1, 1),
                (1, 1),
                (0, 0),
                (0, 0),
                (2, 2),
                (0, 0),
                (3, 3),
            ],
            [
                (3, 3),
                (1, 1),
                (0, 0),
                (2, 2),
                (0, 0),
                (2, 1),
                (1, 1),
                (1, 3),
                (3, 3),
            ],
            [
                (3, 3),
                (0, 0),
                (1, 1),
                (2, 1),
                (2, 1),
                (0, 0),
                (0, 0),
                (0, 0),
                (3, 3),
            ],
            [
                (3, 3),
                (0, 0),
                (1, 1),
                (0, 0),
                (1, 1),
                (0, 0),
                (0, 0),
                (0, 0),
                (3, 3),
            ],
            [
                (3, 3),
                (2, 1),
                (2, 1),
                (0, 0),
                (1, 1),
                (2, 1),
                (1, 1),
                (0, 0),
                (3, 3),
            ],
            [
                (3, 3),
                (3, 3),
                (3, 3),
                (3, 3),
                (3, 3),
                (3, 3),
                (3, 3),
                (3, 3),
                (3, 3),
            ],
        ]

    def test_find_adjacent(self):
        adjacent_positions = find_adjacent(1, 1)
        self.assertEqual(adjacent_positions, [[0, 1], [1, 0], [1, 2], [2, 1]])

    def test_check_player_hinges(self):
        hinges = check_player_hinges(
            board=self.game.board["data"], row_number=1, col_number=3
        )
        self.assertEqual(hinges, True)
        hinges = check_player_hinges(
            board=self.game.board["data"], row_number=6, col_number=7
        )
        self.assertEqual(hinges, False)
        hinges = check_player_hinges(
            board=self.game.board["data"], row_number=6, col_number=7
        )
        self.assertEqual(hinges, False)
        hinges = check_player_hinges(
            board=self.game.board["data"], row_number=7, col_number=7
        )
        self.assertEqual(hinges, False)

    def test_hinge_check(self):
        hinges = hinge_check(self.game.board["data"], row_number=1, col_number=1)
        self.assertEqual(hinges, 3)
        hinges = hinge_check(self.game.board["data"], row_number=7, col_number=6)
        self.assertEqual(hinges, 2)
        hinges = hinge_check(self.game.board["data"], row_number=4, col_number=5)
        self.assertEqual(hinges, 1)

    def test_check_adjacent_stones(self):
        # Check a known position that would cause a stone to have 4 hinges
        creates_4_hinges = check_adjacent_stones(
            self.game.board["data"], row_number=6, col_number=3
        )
        self.assertEqual(creates_4_hinges, True)
        # Check a known position that would cause a stone to have 4 hinges
        creates_4_hinges = check_adjacent_stones(
            self.game.board["data"], row_number=2, col_number=1
        )
        self.assertEqual(creates_4_hinges, True)
        # Check a known position that should not cause a stone to have 4 hinges
        creates_4_hinges = check_adjacent_stones(
            self.game.board["data"], row_number=5, col_number=5
        )
        self.assertEqual(creates_4_hinges, False)

    def test_check_score(self):
        self.assertEqual(
            check_score(board=self.game.board["data"], score_type=0, player=1), 11
        )
        self.assertEqual(
            check_score(board=self.game.board["data"], score_type=0, player=2), 8
        )
        self.assertEqual(
            check_score(board=self.game.board["data"], score_type=1, player=1), 19
        )
        self.assertEqual(
            check_score(board=self.game.board["data"], score_type=1, player=2), 16
        )

    def test_remaining_moves(self):
        possible_moves = remaining_moves(self.game.board["data"])
        self.assertEqual(
            possible_moves,
            [[3, 1], [4, 4], [5, 1], [5, 5], [5, 7], [6, 6], [6, 7], [7, 7]],
        )

    def test_check_thunder_stone(self):
        self.assertEqual(check_thunder_stone(self.game, row=3, col=1), True)
        self.assertEqual(check_thunder_stone(self.game, row=1, col=1), False)
        self.assertEqual(check_thunder_stone(self.game, row=2, col=6), False)

    def test_check_woden_stone(self):
        # Check a location occupied by the active player's stone
        self.assertEqual(check_woden_stone(self.game, row=1, col=1), False)
        # Check a location occupied by an opponent's stone
        self.assertEqual(check_woden_stone(self.game, row=1, col=5), True)
        # Check an empty square
        self.assertEqual(check_woden_stone(self.game, row=2, col=1), False)
        # Check an invalid board position
        self.assertEqual(check_woden_stone(self.game, row=13, col=2), False)

    def test_check_valid_move(self):
        # Check various positions with a standard stone being active
        self.game.active_stone = 1
        self.assertEqual(valid_move(self.game, row=1, col=1), False)
        self.assertEqual(valid_move(self.game, row=0, col=0), False)
        self.assertEqual(valid_move(self.game, row=6, col=6), True)
        # Check various positions with a thunder-stone being active
        self.game.active_stone = 2
        self.assertEqual(check_thunder_stone(self.game, row=3, col=1), True)
        self.assertEqual(check_thunder_stone(self.game, row=1, col=1), False)
        self.assertEqual(check_thunder_stone(self.game, row=2, col=6), False)
        # Check various positions with a woden-stone being active
        self.game.active_stone = 3
        self.assertEqual(check_woden_stone(self.game, row=4, col=1), False)
        self.assertEqual(check_woden_stone(self.game, row=1, col=5), True)
        self.assertEqual(check_woden_stone(self.game, row=2, col=1), False)
        self.assertEqual(check_woden_stone(self.game, row=13, col=2), False)
