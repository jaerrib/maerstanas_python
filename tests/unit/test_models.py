import unittest

from app.board import Board
from app.game import Game


class TestBoaerd(unittest.TestCase):

    def test_new_board(self):
        board = Board()
        self.assertEqual(
            board.data,
            [
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
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (3, 3),
                ],
                [
                    (3, 3),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (3, 3),
                ],
                [
                    (3, 3),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (3, 3),
                ],
                [
                    (3, 3),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (3, 3),
                ],
                [
                    (3, 3),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (3, 3),
                ],
                [
                    (3, 3),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (3, 3),
                ],
                [
                    (3, 3),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
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
            ],
        )


class TestGame(unittest.TestCase):

    def test_new_game(self):
        game = Game()
        self.assertEqual(game.move_list, [])
        self.assertEqual(game.score_p1, 0)
        self.assertEqual(game.score_p2, 0)
        self.assertEqual(game.result, "")
        self.assertEqual(game.active_player, 1)
        self.assertEqual(game.active_stone, 1)
        self.assertEqual(game.scoring_type, 1)
        self.assertEqual(game.ruleset, "0.4")
        self.assertEqual(
            game.special_stones,
            {
                "player1": [1, 2, 3],
                "player2": [1, 2, 3],
            },
        )


if __name__ == "__main__":
    unittest.main()
