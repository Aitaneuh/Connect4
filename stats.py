from player import Player

class Stat:
    def __init__(self, winner: str, moves: int, orentation: str, is_first_player: str ):
        self.winner = winner
        self.moves = moves
        self.orientation = orentation
        self.is_first_player = is_first_player