from player import Player

class HumanPlayer(Player):
    def get_move(self, board) -> int:
        while True:
            try:
                col = int(input(f"{self.name} ({self.piece}), choose a column: "))
                if 0 <= col < len(board[0]):
                    return col
                else:
                    print("Invalid column. Try again.")
            except ValueError:
                print("Please enter a number.")