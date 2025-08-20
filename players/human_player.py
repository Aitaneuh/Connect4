from player import Player

class HumanPlayer(Player):
    def play(self, board: list[list[str]], valid_moves: list[int]) -> int:
        while True:
            try:
                col = int(input(f"{self.name} ({self.piece}), choose a column: "))
                if col in valid_moves:
                    return col
                else:
                    print("Invalid column. Try again.")
            except ValueError:
                print("Please enter a number.")