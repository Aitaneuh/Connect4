from player import Player
import random

class RandomAgent(Player):
    def play(self, board: list[list[str]], valid_moves: list[int]) -> int:
        res = random.choice(valid_moves)
        piece = self.piece
        # TODO make win and loose possiblities algo
        return res