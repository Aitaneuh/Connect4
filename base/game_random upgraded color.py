import random as rnd
import copy

ROWS = 6
COLUMNS = 7

def create_board():
    return [["  " for cols in range(COLUMNS)] for rows in range(ROWS)]

def print_board(board):
    print("\n  0  1  2  3  4  5  6")
    print("+" + "---"*(COLUMNS-1) + "--" + "+")
    for row in board:
        print("|" + "|".join(row) + "|")
    print("+" + "---"*(COLUMNS-1) + "--" + "+\n")

def is_valid_move(board, col):
    """Vérifie si la colonne choisie est vide"""
    return board[0][col] == "  "

def get_next_open_row(board, col):
    """Retourne la ligne disponible dans la colonne choisie"""
    for r in range(ROWS-1, -1, -1):
        if board[r][col] == "  ":
            return r

def drop_piece(board, row, col, piece):
    """Place le jeton dans le plateau"""
    if piece == "X":
        piece = "🔴"
    else:
        piece = "🟡"
        
    board[row][col] = piece

def winning_move(board, piece):
    """Vérifie si le joueur a gagné"""
    # Vérifie horizontalement
    if piece == "X":
        piece = "🔴"
    else:
        piece = "🟡"
    for c in range(COLUMNS-3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return c
    # Vérifie verticalement
    for c in range(COLUMNS):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return c
    # Vérifie diagonalement (haut-gauche à bas-droite)
    for c in range(COLUMNS-3):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return c
    # Vérifie diagonalement (bas-gauche à haut-droite)
    for c in range(COLUMNS-3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return c
    return -1

def main():
    board = create_board()
    game_over = False
    turn = 0  # 0 pour joueur 1, 1 pour joueur 2
    print_board(board)

    while not game_over:
        # Demande au joueur courant de choisir une colonne
        if turn == 0:
            col = int(input("Joueur 1 (🔴), choisis une colonne (0-6): "))
            piece = "X"
        else:
            piece = "O"
            col = rnd.randint(0, 6)

            force_move = False
            for c in range(COLUMNS):
                clone_board = copy.deepcopy(board)
                if is_valid_move(clone_board, c):
                    row = get_next_open_row(clone_board, c)
                    drop_piece(clone_board, row, c, piece)
                    if winning_move(clone_board, piece) != -1:
                        col = c
                        force_move = True
                        break
            if not force_move:
                piece = "X"
                for c in range(COLUMNS):
                    clone_board = copy.deepcopy(board)
                    if is_valid_move(clone_board, c):
                        row = get_next_open_row(clone_board, c)
                        drop_piece(clone_board, row, c, piece)
                        if winning_move(clone_board, piece) != -1:
                            col = c
                            break
            piece = "O"


        if 0 <= col <= COLUMNS-1:
            if is_valid_move(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, piece)
                print_board(board)

                if winning_move(board, piece) != -1:
                    if piece == "X":
                        piece = "🔴"
                    else:
                        piece = "🟡"
                    print(f"Félicitations ! Joueur {turn+1} ({piece}) a gagné !")
                    game_over = True
                else:
                    # Change de joueur
                    turn = (turn + 1) % 2
            else:
                print("Colonne pleine, choisis-en une autre.")
        else:
            print("Colonne invalide. Choisis un nombre entre 0 et 6.")
        """debug"""
        # print(board) 
        

if __name__ == "__main__":
    main()
