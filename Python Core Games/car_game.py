# Car Game

command = ""

while True:
    command = input("> ").lower()
    if command == "start":
        print("Car is started...")
    elif command == "stop":
        print("Car is stopped...")
    elif command == "help":
        print("""
        Command to play the Game:
        start - to start the car
        stop - to stop the car
        quit - to quit the game
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand your keyword take help command.")