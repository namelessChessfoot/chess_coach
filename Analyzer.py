import chess
from chess import pgn, engine
from chess import Board


class Analyzer:
    def __init__(self, game: pgn.Game, engine: engine.SimpleEngine):
        self.game = game
        self.engine = engine

    def analyzeSinglePosition(self, board: Board):
        return (
            self.engine.analyse(board, engine.Limit(time=0.1))["score"]
            .pov(chess.WHITE)
            .score(mate_score=7000)
        )

    def analyze(self):
        board = self.game.board()
        res = [self.analyzeSinglePosition(board)]
        for move in self.game.mainline_moves():
            board.push(move)
            res.append(self.analyzeSinglePosition(board))
        return res
