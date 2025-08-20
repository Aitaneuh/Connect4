from game import Game

main = Game()

print(main)
print(main.check_win("X"))

for i in range(4):
    main.board[5][i] = "X"

print(main)
print(main.check_win("X"))

main.reset()
print(main)

for i in range(4):
    main.board[5-i][6] = "O"

print(main)
print(main.check_win("O"))