from abc import ABC, abstractmethod

class Player:
    def __init__(self, name: str, piece: str):
        self.name = name
        self.piece = piece

    @abstractmethod
    def play(self, board: list[list[str]], valid_moves: list[int]) -> int:
        """Return the column index where the player wants to play"""
        pass