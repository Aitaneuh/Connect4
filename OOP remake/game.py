class InvalidMove(Exception):
    pass

class Game:
    ROWS = 6
    COLUMNS = 7
    EMPTY = " "

    def __init__(self):
        self.board = [[self.EMPTY for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]

    def __str__(self):
        """Return the Board formated"""

        res = ("\n 0 1 2 3 4 5 6")
        res += ("\n+" + "--"*(self.COLUMNS) + "-" + "+")
        for row in self.board:
            res += ("\n|" + "|".join(row) + "|")
        res += "\n+" + "--"*(self.COLUMNS) + "-" + "+\n"
        return res
    
    def check_win(self, piece: str) -> tuple[bool, str | None]:
        """Check if a type of piece has won"""
        for c in range(self.COLUMNS-3):
            for r in range(self.ROWS):
                if all(self.board[r][c+i] == piece for i in range(4)):
                    return (True, "hor")

        for c in range(self.COLUMNS):
            for r in range(self.ROWS-3):
                if all(self.board[r+i][c] == piece for i in range(4)):
                    return (True, "ver")

        for c in range(self.COLUMNS-3):
            for r in range(self.ROWS-3):
                if all(self.board[r+i][c+i] == piece for i in range(4)):
                    return (True, "diag")

        for c in range(self.COLUMNS-3):
            for r in range(3, self.ROWS):
                if all(self.board[r-i][c+i] == piece for i in range(4)):
                    return (True, "diag")

        return (False, None)
    
    def clear_board(self) -> None:
        """Reset the game to original state"""
        self.board = [[self.EMPTY for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]
        return

    def _is_valid_move(self, col: int):
        """Check if a move is valid"""
        if self.board[0][col] == self.EMPTY:
            return True
        else:
            return False
        
    def drop_piece(self, col: int, piece: str) -> None:
        """Drop a piece of the selected type in the selected column, return False if not possible"""
        if not self._is_valid_move(col):
            raise InvalidMove(f"Column {col} is full")
        row = self._get_next_open_row(col)
        if row is not None:
            self.board[row][col] = piece

    

    def _get_next_open_row(self, col: int) -> int | None:
        """Get the most up row on a column"""
        for r in range(self.ROWS-1, -1, -1):
            if self.board[r][col] == self.EMPTY:
                return r

        return None
    
    def is_board_full(self) -> bool:
        """Check if the board is full"""
        return all(cell != self.EMPTY for row in self.board for cell in row)
