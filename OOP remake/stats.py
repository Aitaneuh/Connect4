from player import Player

class Stat:
    def __init__(self, winner: Player | str, moves: int, orentation: str | None):
        self.winner = winner
        self.moves = moves
        self.orentation = orentation