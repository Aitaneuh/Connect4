from player import Player
import random

class RandomAgent(Player):
    def play(self, board: list[list[str]], valid_moves: list[int]) -> int:
        return random.choice(valid_moves)