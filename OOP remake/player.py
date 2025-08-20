from abc import ABC, abstractmethod

class Player:
    def __init__(self, name: str, piece: str):
        self.name = name
        self.piece = piece

    @abstractmethod
    def get_move(self, board):
        """Return the column index where the player wants to play"""
        pass