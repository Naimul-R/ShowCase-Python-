def show_player(name, sport):
    print(f"Player: {name} | Sports: {sport}")

def add_score(player, score):
    print(f"{player} socred {score} points.")

def is_winner(player, score):
    if score > 10:
        print(f"{player} WINS! 🏆")
    else:
        print(f"{player} needs more points! 💪")

# --- Calling the functions ---
show_player("Fede Valvarde", "Football")
add_score("Fede Valvarde", 3)
is_winner("Ali", 3)