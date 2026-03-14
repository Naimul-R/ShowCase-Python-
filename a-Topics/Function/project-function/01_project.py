def add_player():
    players = []

    for i in range(1, 4):
        name = input(f"Enter player {i} name: ")
        score = int(input(f"Enter player {i} score: "))

        players.append ({
            "name": name,
            "score": score
        })

    return players

def show_leaderboard(players):
    print("\n--- Sports Leaderboard ---")

    for i, player in enumerate(players, 1):
        print(f"{i}. {player['name']:<10} - Score: {player['score']}")

    print("--------------------------")

def get_winner(players):
    winner = players[0]

    for player in players:
        if player["score"] > winner["score"]:
            winner = player

    return winner 

def full_leaderboard():
    players = add_player()
    show_leaderboard(players)
    winner = get_winner(players)

    print(f"\nWinner is {winner['name']} with score {winner['score']}! 🏆")

full_leaderboard()