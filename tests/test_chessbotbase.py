import unittest
import chess

from base.ChessBotBase import Bot


class TinyBot(Bot):
    def setup(self):
        self.name = "Tiny Bot"

    def evaluate(self, board):
        return 0


class ChessBotBaseTests(unittest.TestCase):
    def test_choose_move_returns_legal_move(self):
        bot = TinyBot(color=chess.WHITE, depth=2, qsearch=False)
        board = chess.Board()

        move = bot.choose_move(board)

        self.assertIsNotNone(move)
        self.assertIn(move, board.legal_moves)

    def test_quiescence_handles_check_positions(self):
        bot = TinyBot(color=chess.WHITE, depth=2, qsearch=True, qdepth=2)
        board = chess.Board("7k/6Q1/6K1/8/8/8/8/8 w - - 0 1")

        score = bot.quiescence(board, 2, -1e9, 1e9)

        self.assertIsInstance(score, (int, float))


if __name__ == "__main__":
    unittest.main()
