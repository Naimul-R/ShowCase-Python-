name = input("Type your name: ")
print(f"Hello {name} welcome to my game!")

should_play = input("Do you wnat to play (y/n): ").lower()

if should_play == "y" or should_play == "yes":
    print("Play continute!")

    direction = input("Do you want to go left or right? (left/right) : ").lower()

    # Left Path ------->
    if direction == "left":
        print("Okey! You went left and entered a dark forest...")
        torch = input("You see a torch on the ground. Do you pick it up? (yes/no) : ").lower()

        if torch == "yes":
            print("Smart move! You now have a torch\n")
            cave = input("You see cave ahead. Do you enter? (yes/no): ").lower()
            if cave == "yes":
                print(f"You explore the cave with your torch and find a treasure chest, {name}! YOU WIN!")
            else:
                print("You stayed outside and a wolf found you. Game over!")
        else:
            cave = input("You see cave ahead. Do you enter? (yes/no): ").lower()
            if cave == "yes":
                print("It's pitch black inside. You trip and fall into a hole. Game over!")
            else:
                print("You stayed outside and a wolf found you. Game over!")

    # Rigt path ------->
    elif direction == "right":
        choice = input("Okey! You now see a bridge. Do you want to swim under it or cross it? (swim/cross) : ").lower()
        if choice == "swim":
            print("You got eaten by a alligator, you die, the end!!")
        else: 
            print("You fonud the gold. And you win!!")
    else: 
        print("Sorry! Not a valid reply. You die!!")

else: 
    print("We are NOT playing...")