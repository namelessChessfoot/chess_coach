from urllib import request
import json, io

import chess, chess.engine, chess.pgn
from Analyzer import Analyzer
import matplotlib.pyplot as plt


def getArchives(username):
    res = request.urlopen(f"https://api.chess.com/pub/player/{username}/games/archives")
    return json.loads(res.read().decode())["archives"]


def getGame(username):
    arch = getArchives(username)[-1]
    res = request.urlopen(arch)
    return json.loads(res.read().decode())["games"][-1]


game = getGame("ILGT")
pgn = io.StringIO(game["pgn"])
game = chess.pgn.read_game(pgn)
engine = chess.engine.SimpleEngine.popen_uci("./engines/stockfish")
analyzer = Analyzer(game, engine)
res = analyzer.analyze()
engine.quit()
plt.plot(res, marker="o")
plt.show()
