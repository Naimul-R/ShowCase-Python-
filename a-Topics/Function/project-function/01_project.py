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

def showleaderboard(players):
    print("\n--- Sports Leaderboard ---")

    for i, player in enumerate(players, 1):
        print(f"{i}. {player['name']:<10} - Score: {player['score']}")

    print("--------------------------")
