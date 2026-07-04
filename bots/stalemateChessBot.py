from base.ChessBotBase import Bot
import chess

class Bot(Bot):
    def setup(self):
        self.name = "Stalemate Bot"

    def evaluate(self, board):
        if board.is_stalemate():
            return 100
        return 0
