from game import Game

def print_debug_text(text: str) -> None:
    print(f"\n////////////////\n\n{text}")
    return 

main = Game()

print_debug_text("board is empty when creating")
print(main)
print(main.check_win("X"))

for i in range(4):
    main.board[5][i] = "X"

print_debug_text("check_win works")
print(main)
print(main.check_win("X"))

print_debug_text("reset works")
main.clear_board()
print(main)

# for i in range(6):
#     main.board[5-i][6] = "O"
# print_debug_text("is_valid_move works")
# print(main)
# print(main.is_valid_move(6))

print_debug_text("Drop a piece works")
main.clear_board()
main.drop_piece(1, "X")
for _ in range(6):
    main.drop_piece(3, "O")
print(main)

print_debug_text("is_board_full works")
main.clear_board()
for i in range(7):
    for _ in range(6):
        main.drop_piece(i, "X")
print(main)
print(main.is_board_full())
