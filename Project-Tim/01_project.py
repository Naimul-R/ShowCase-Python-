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
        print("You see a bridge ahead...\n")
        choice = input("Okey! You now see a bridge. Do you want to swim under it or cross it? (swim/cross) : ").lower()
        if choice == "swim":
            print("You got eaten by a alligator, you die, the end!!")
        elif choice == "cross":
            print("You crossed the bridge safely!\n")
            next_choice = input("You now see a cave and a village. Where do you go? (cave/village): ").lower()

            if next_choice == "cave":
                riddle = input("A troll blocks the cave! He asks: 'What has legs but cannot walk?' (answer): ").lower()
                if riddle == "table" or riddle == "a table":
                    print(f"The troll steps aside. You enter the cave and find the gold, {name}! YOU WIN!")
                else:
                    print("Wrong answer! The troll throws you off the bridge. Game over!")
                    
            elif next_choice == "village":
                print("You entered the village.")
                villager = input("A villager offers you a map or a sword. Which do you take? (map/sword): ").lower()
                if villager == "map":
                    print(f"The map leads you straight to the hidden treasure, {name}! YOU WIN!")
                elif villager == "sword":
                    print("You took the sword but got lost in the woods forever. Game over!")
                else:
                    print("You couldn't decide and the village gates closed. Game over!")
            else:
                print("You stood there confused and it got dark. Game over!")
        else:
            print("Not a valid choice. You slipped into the river. Game over!")

    # Forward Path ------>
    elif direction == "forward":
        print("You walk forward and reach a mysterious castle!\n")
        enter = input("Do you knock on the door or sneak around the back? (knock/sneak): ").lower()

        if enter == "knock":
            print("A friendly wizard open the door\n")
            quest = input("He says: 'Solve my puzzle and I will reward you. 2 + 2 x 2 = ?' (answer): ")
            if quest == "6":
                print(f"Correct! The wizard gives you a chest full of gold, {name}! YOU WIN!")
            else:
                print("Wrong! The wizard turns you into a frog. Game over!")

        if enter == "sneak":
            print("You sneak around the back and find a locked door.\n")
            key = input("There is a key under the mat. Do you use it? (yes/no): ").lower()
            if key == "yes":
                print(f"You unlock the door and find the royal treasure room, {name}! YOU WIN!")
            else:
                print("You walked away and never found the treasure. Game over!")

        else:
            print("You stood frozen and the castle gates crushed you. Game over!")

    # Invalid direction ------>
    else:
        print("Not a valid direction. You wandered off and got lost. Game over!")

else:
    print("We are NOT playing...")