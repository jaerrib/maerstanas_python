import unittest

from app.ai_player import *
from app.game import Game


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

    def test_is_corner(self):
        self.assertEqual(is_corner([1, 1], self.game.board.data), True)
        self.assertEqual(is_corner([1, 7], self.game.board.data), True)
        self.assertEqual(is_corner([7, 1], self.game.board.data), True)
        self.assertEqual(is_corner([7, 7], self.game.board.data), True)
        self.assertEqual(is_corner([1, 2], self.game.board.data), False)
        self.assertEqual(is_corner([3, 5], self.game.board.data), False)

    def test_is_edge(self):
        self.assertEqual(is_edge([1, 1], self.game.board.data), False)
        self.assertEqual(is_edge([1, 2], self.game.board.data), True)
        self.assertEqual(is_edge([7, 3], self.game.board.data), True)
        self.assertEqual(is_edge([3, 5], self.game.board.data), False)

    def test_hinges_created(self):
        self.assertEqual(
            hinges_created(move=[6, 6], board=self.game.board.data, active_player=1), 1
        )
        self.assertEqual(
            hinges_created(move=[7, 7], board=self.game.board.data, active_player=1), 1
        )
        self.assertEqual(
            hinges_created(move=[6, 6], board=self.game.board.data, active_player=2), 0
        )
        self.assertEqual(
            hinges_created(move=[5, 1], board=self.game.board.data, active_player=1), 2
        )
        self.assertEqual(
            hinges_created(move=[5, 5], board=self.game.board.data, active_player=2), 2
        )

    def test_stones_blocked(self):
        self.assertEqual(
            stones_blocked(move=[5, 5], board=self.game.board.data, active_player=1), 2
        )
        self.assertEqual(
            stones_blocked(move=[5, 5], board=self.game.board.data, active_player=2), 0
        )
        self.assertEqual(
            stones_blocked(move=[5, 7], board=self.game.board.data, active_player=2), 1
        )
        self.assertEqual(
            stones_blocked(move=[6, 7], board=self.game.board.data, active_player=2), 0
        )

    def test_stones_removed(self):
        self.assertEqual(
            stones_removed(move=[1, 2], board=self.game.board.data, active_player=1),
            (2, 0),
        )
        self.assertEqual(
            stones_removed(move=[3, 7], board=self.game.board.data, active_player=1),
            (1, 2),
        )
        self.assertEqual(
            stones_removed(move=[4, 2], board=self.game.board.data, active_player=1),
            (3, 1),
        )
        self.assertEqual(
            stones_removed(move=[3, 5], board=self.game.board.data, active_player=2),
            (3, 0),
        )
