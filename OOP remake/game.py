class Game:
    board = [[" " for cols in range(7)] for rows in range(6)]

    def __str__(self):
        """Return the Board formated"""

        res = ("\n 0 1 2 3 4 5 6")
        res += ("\n+" + "--"*(6) + "-" + "+")
        for row in self.board:
            res += ("\n|" + "|".join(row) + "|")
        res += "\n+" + "--"*(6) + "-" + "+\n"
        return res
    
    def check_win(self, piece) -> tuple[bool, str | None]:
        """Check if a type of piece has won"""
        for c in range(7-3):
            for r in range(6):
                if all(self.board[r][c+i] == piece for i in range(4)):
                    return (True, "hor")

        for c in range(7):
            for r in range(6-3):
                if all(self.board[r+i][c] == piece for i in range(4)):
                    return (True, "ver")

        for c in range(7-3):
            for r in range(6-3):
                if all(self.board[r+i][c+i] == piece for i in range(4)):
                    return (True, "diag")

        for c in range(7-3):
            for r in range(3, 6):
                if all(self.board[r-i][c+i] == piece for i in range(4)):
                    return (True, "diag")

        return (False, None)
    
    def reset(self) -> None:
        """Reset the game to original state"""
        self.board = [[" " for cols in range(7)] for rows in range(6)]
        return


