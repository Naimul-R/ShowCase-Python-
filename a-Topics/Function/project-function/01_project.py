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