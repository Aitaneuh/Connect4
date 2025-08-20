import matplotlib.pyplot as plt
from collections import Counter
from stats import Stat

def draw_graphs(stats: list[Stat]) -> None:
    """Draw matplotlib graphs with the stats"""
    moves = [stat.moves for stat in stats]
    orientations = [stat.orientation for stat in stats]
    winners = [stat.winner for stat in stats]
    first_player_result = [stat.is_first_player if stat.is_first_player is not None else "draw" for stat in stats]


    orientation_counts = Counter(orientations)
    winner_counts = Counter(winners)
    first_player_counts = Counter(first_player_result)

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    axes[0,0].bar(list(first_player_counts.keys()), list(first_player_counts.values()), color=['skyblue','salmon','lightgray'])
    axes[0,0].set_title("First Player Win / Lose / Draw")
    axes[0,0].set_ylabel("Number of Games")
    total_games = sum(first_player_counts.values())
    for i, key in enumerate(first_player_counts.keys()):
        count = first_player_counts[key]
        percent = (count / total_games) * 100
        axes[0,0].text(i, count + 0.1, f"{percent:.1f}%", ha='center', va='bottom')

    axes[0,1].hist(moves, bins=range(min(moves), max(moves)+2), color='lightgreen', edgecolor='black')
    axes[0,1].set_title("Histogram of Moves per Game")
    axes[0,1].set_xlabel("Number of Moves")
    axes[0,1].set_ylabel("Frequency")

    axes[1,0].bar(list(orientation_counts.keys()), list(orientation_counts.values()), color=['skyblue','salmon','lightgray'])
    axes[1,0].set_title("Distribution of Victory Orientations")
    axes[1,0].set_xlabel("Orientation")
    axes[1,0].set_ylabel("Number of Games")

    axes[1,1].pie(list(winner_counts.values()), labels=list(winner_counts.keys()), autopct='%1.1f%%', startangle=90)
    axes[1,1].set_title("Wins per Player")

    plt.tight_layout()
    plt.show()