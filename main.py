from game import Game
from player import Player
from stats import Stat
from players.human_player import HumanPlayer
from players.random_agent import RandomAgent
from players.smart_agent import SmartAgent
import random
import time

while True:
    mode = int(input("\nChoose what mode you want to play :\n\n\t1. Player vs Player\n\t2. Player vs Agent\n\t3. Agent vs Agent\n\t4. Agent vs Agent with stats\n\nmode selected : "))
    if mode in [1, 2, 3, 4]:
        break
    print("You have to choose your game mode between 1, 2, 3 and 4")

if mode == 1:
    name_player1 = input("Enter the name of the first player : ")
    player1 = HumanPlayer(name_player1,"X")
    name_player2 = input("Enter the name of the second player : ")
    player2 = HumanPlayer(name_player2,"O")
elif mode == 2:
    name_player = input("Enter your name : ")
    player1 = HumanPlayer(name_player,"X")
    while True:
        agent_selected = int(input("\nSelect against which agent do you want to play :\n\n\t1. Full Random Agent\n\t2. Smart Algo Agent\n\t3. Ai Machine Learning Agent\n\nagent selected : "))
        if agent_selected in [1, 2]:
            break
        elif agent_selected == 3:
            print("This one is not quit ready yet")
        else:
            print("You have to choose your agent between 1 and 2")
    
    if agent_selected == 1:
        player2 = RandomAgent("Random man", "O")
    elif agent_selected == 2:
        player2 = SmartAgent("Smart guy", "O")

elif mode == 3 or mode == 4:
    while True:
        agent_selected1 = int(input("\nSelect the first agent (play with \"O\") :\n\n\t1. Full Random Agent\n\t2. Smart Algo Agent\n\t3. Ai Machine Learning Agent\n\nagent selected : "))
        if agent_selected1 in [1, 2]:
            break
        elif agent_selected1 == 3:
            print("This one is not quit ready yet")
        else:
            print("You have to choose your agent between 1 and 2")
    if agent_selected1 == 1:
        player1 = RandomAgent("Random man", "O")
    elif agent_selected1 == 2:
        player1 = SmartAgent("Smart guy", "O")
    while True:
        agent_selected2 = int(input("\nSelect the second agent (play with \"X\") :\n\n\t1. Full Random Agent\n\t2. Smart Algo Agent\n\t3. Ai Machine Learning Agent\n\nagent selected : "))
        if agent_selected2 in [1, 2]:
            break
        elif agent_selected2 == 3:
            print("This one is not quit ready yet")
        else:
            print("You have to choose your agent between 1 and 2")
    if agent_selected2 == 1:
        player2 = RandomAgent("Random man", "X")
    elif agent_selected2 == 2:
        player2 = SmartAgent("Smart guy", "X")

game = Game()

if mode != 4:
    def turn(player: Player) -> bool:
        print(game)
        valid_moves = game.get_valid_moves()
        col = player.play(game.board, valid_moves)
        game.drop_piece(col, player.piece)
        if game.check_win(player.piece)[0] != False:
            print(game)
            print(f"{player.name} won the match")
            return True
        if game.is_board_full():
            print(game)
            print("The board is full, let's reset it")
            game.clear_board()
        if mode == 3:
            time.sleep(0.5)
        return False

    first_to_play = random.choice([True,False])

    while True:
        if first_to_play:
            if turn(player1): break
            if turn(player2): break
        else:
            if turn(player2): break
            if turn(player1): break
else:
    iteration = int(input("\nEnter the number of games that you want to simulate : "))
    stats = []

    for i in range(iteration):
        game.clear_board()

        def play_one_game():
            moves = 0

            def stat_turn(player: Player) -> bool:
                nonlocal moves
                moves += 1
                valid_moves = game.get_valid_moves()
                col = player.play(game.board, valid_moves)
                game.drop_piece(col, player.piece)
                game_check = game.check_win(player.piece)
                if game_check[0] != False:
                    stats.append(Stat(player, moves, game_check[1]))
                    return True
                if game.is_board_full():
                    stats.append(Stat("Draw", moves, None))
                    return True
                return False

            first_to_play = random.choice([True, False])

            while True:
                if first_to_play:
                    if stat_turn(player1): break
                    if stat_turn(player2): break
                else:
                    if stat_turn(player2): break
                    if stat_turn(player1): break

        play_one_game()
        print(f"{i}/{iteration}")
        
    for stat in stats:
        print(f"{stat.winner.name} | {stat.moves} | {stat.orentation}")

