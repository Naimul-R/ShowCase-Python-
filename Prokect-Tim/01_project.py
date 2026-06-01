name = input("Type your name: ")
print(f"Hello {name} welcome to my game!")

should_play = input("Do you wnat to play (y/n): ").lower()

if should_play == "y" or should_play == "yes":
    print("Play continute!")

    direction = input("Do you want to go left or right: ").lower()
    if direction == "left":
        print("Okey! We went left.")
    else: 
        print("Okey! We went right.")

else: 
    print("We are NOT playing...")