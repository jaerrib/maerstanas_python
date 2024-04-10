import unittest

from app.game import Game
from app.game_logic import *


class GameLogicTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.board.data = [
            [
                [3, 3],
                [3, 3],
                [3, 3],
                [3, 3],
                [3, 3],
                [3, 3],
                [3, 3],
                [3, 3],
                [3, 3],
            ],
            [
                [3, 3],
                [1, 1],
                [1, 1],
                [0, 0],
                [1, 1],
                [2, 1],
                [0, 0],
                [2, 1],
                [3, 3],
            ],
            [
                [3, 3],
                [0, 0],
                [1, 1],
                [1, 1],
                [1, 1],
                [2, 2],
                [2, 2],
                [2, 2],
                [3, 3],
            ],
            [
                [3, 3],
                [0, 0],
                [1, 1],
                [1, 1],
                [0, 0],
                [0, 0],
                [2, 2],
                [0, 0],
                [3, 3],
            ],
            [
                [3, 3],
                [1, 1],
                [0, 0],
                [2, 2],
                [0, 0],
                [2, 1],
                [1, 1],
                [1, 3],
                [3, 3],
            ],
            [
                [3, 3],
                [0, 0],
                [1, 1],
                [2, 1],
                [2, 1],
                [0, 0],
                [0, 0],
                [0, 0],
                [3, 3],
            ],
            [
                [3, 3],
                [0, 0],
                [1, 1],
                [0, 0],
                [1, 1],
                [0, 0],
                [0, 0],
                [0, 0],
                [3, 3],
            ],
            [
                [3, 3],
                [2, 1],
                [2, 1],
                [0, 0],
                [1, 1],
                [2, 1],
                [1, 1],
                [0, 0],
                [3, 3],
            ],
            [
                [3, 3],
                [3, 3],
                [3, 3],
                [3, 3],
                [3, 3],
                [3, 3],
                [3, 3],
                [3, 3],
                [3, 3],
            ],
        ]

    def test_col_conversion(self):
        self.assertEqual(convert_num_to_col(1), "A")
        self.assertEqual(convert_num_to_col(2), "B")
        self.assertEqual(convert_num_to_col(3), "C")
        self.assertEqual(convert_num_to_col(4), "D")
        self.assertEqual(convert_num_to_col(5), "E")
        self.assertEqual(convert_num_to_col(6), "F")
        self.assertEqual(convert_num_to_col(7), "G")
        self.assertNotEqual(convert_num_to_col(1), "B")
        self.assertNotEqual(convert_num_to_col(0), "A")

    def test_find_adjacent(self):
        adjacent_positions = find_adjacent(1, 1)
        self.assertEqual(adjacent_positions, [[0, 1], [1, 0], [1, 2], [2, 1]])

    def test_check_player_hinges(self):
        hinges = check_player_hinges(
            board=self.game.board.data, row_number=1, col_number=3
        )
        self.assertEqual(hinges, True)
        hinges = check_player_hinges(
            board=self.game.board.data, row_number=6, col_number=7
        )
        self.assertEqual(hinges, False)
        hinges = check_player_hinges(
            board=self.game.board.data, row_number=6, col_number=7
        )
        self.assertEqual(hinges, False)
        hinges = check_player_hinges(
            board=self.game.board.data, row_number=7, col_number=7
        )
        self.assertEqual(hinges, False)

    def test_hinge_check(self):
        hinges = hinge_check(self.game.board.data, row_number=1, col_number=1)
        self.assertEqual(hinges, 3)
        hinges = hinge_check(self.game.board.data, row_number=7, col_number=6)
        self.assertEqual(hinges, 2)
        hinges = hinge_check(self.game.board.data, row_number=4, col_number=5)
        self.assertEqual(hinges, 1)

    def test_check_adjacent_stones(self):
        position = check_adjacent_stones(
            self.game.board.data, row_number=5, col_number=6
        )
        self.assertEqual(position, True)
        position = check_adjacent_stones(
            self.game.board.data, row_number=6, col_number=5
        )
        self.assertEqual(position, True)
        position = check_adjacent_stones(
            self.game.board.data, row_number=3, col_number=1
        )
        self.assertEqual(position, False)

    def test_check_default_stone(self):
        self.assertEqual(
            check_default_stone(self.game.board.data, row=10, col=6), False
        )
        self.assertEqual(check_default_stone(self.game.board.data, row=1, col=1), False)
        self.assertEqual(check_default_stone(self.game.board.data, row=3, col=7), False)
        self.assertEqual(check_default_stone(self.game.board.data, row=5, col=6), False)
        self.assertEqual(check_default_stone(self.game.board.data, row=6, col=7), True)

    def test_check_thunder_stone(self):
        self.assertEqual(
            check_thunder_stone(self.game.board.data, row=10, col=10), False
        )
        self.assertEqual(check_thunder_stone(self.game.board.data, row=1, col=1), False)
        self.assertEqual(check_thunder_stone(self.game.board.data, row=3, col=1), True)
        self.assertEqual(check_thunder_stone(self.game.board.data, row=3, col=7), True)

    def test_check_woden_stone(self):
        self.assertEqual(
            check_woden_stone(self.game.board.data, active_player=1, row=10, col=10),
            False,
        )
        self.assertEqual(
            check_woden_stone(self.game.board.data, active_player=1, row=1, col=1),
            False,
        )
        self.assertEqual(
            check_woden_stone(self.game.board.data, active_player=1, row=3, col=1),
            False,
        )
        self.assertEqual(
            check_woden_stone(self.game.board.data, active_player=1, row=3, col=6),
            True,
        )

    def test_remaining_moves(self):
        self.assertEqual(
            remaining_moves(self.game.board.data),
            [[3, 1], [4, 4], [5, 1], [5, 5], [5, 7], [6, 6], [6, 7], [7, 7]],
        )
