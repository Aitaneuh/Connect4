from player import Player
import random

class SmartAgent(Player):
    def get_next_open_row(self, board: list[list[str]], col: int, ROWS: int):
        for r in range(ROWS-1, -1, -1):
            if board[r][col] == " ":
                return r

    def check_critic_move(self, board: list[list[str]], ROWS, COLUMNS, valid_moves: list):
        piece = "X"
        for _ in range(2):
            for col in valid_moves:
                temp_board = [row[:] for row in board]  # deep copy
                next_row = self.get_next_open_row(temp_board, col, ROWS)
                if next_row is None:
                    continue
                temp_board[next_row][col] = piece
                for c in range(COLUMNS-3):
                    for r in range(ROWS):
                        if all(temp_board[r][c+i] == piece for i in range(4)):
                            return (True, c)
                        
                for c in range(COLUMNS):
                    for r in range(ROWS-3):
                        if all(temp_board[r+i][c] == piece for i in range(4)):
                            return (True, c)

                for c in range(COLUMNS-3):
                    for r in range(ROWS-3):
                        if all(temp_board[r+i][c+i] == piece for i in range(4)):
                            return (True, c)

                for c in range(COLUMNS-3):
                    for r in range(3, ROWS):
                        if all(temp_board[r-i][c+i] == piece for i in range(4)):
                            return (True, c)
                        
            piece = "O"
        return (False, None)
        
    def play(self, board: list[list[str]], valid_moves: list[int]) -> int:
        res = random.choice(valid_moves)
        ROWS = len(board)
        COLUMNS = len(board[0])

        critic_move = self.check_critic_move(board, ROWS, COLUMNS, valid_moves)
        if critic_move[0] == True and isinstance(critic_move[1], int):
            res = critic_move[1]

        return res