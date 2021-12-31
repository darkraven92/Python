import random

def randomgame():

    while True:
        score = 0

        print("Welcome to this Number Guessing Game!\n")

        print("Guess a number between")
        print("1. 1-10")
        print("2. 1-100")
        print("3. any range")
        print("4. Show score")
        print("5. Quit")

        user_input = input("> ")

        if user_input == "1":
            print("Guess a number between 1-10")
            number = random.randint(1,10)
            user_guess = int(input("> "))
            while user_guess != number:
                user_guess = int(input("Wrong! Guess again:  "))
            print("You guessed the correct number!")
        
        if user_input == "2":
            print("Guess a number between 1-100")
            number = random.randint(1,100)
            user_guess = int(input("> "))
            while user_guess != number:
                user_guess = int(input("Wrong! Guess again:  "))
            print("You guessed the correct number!")
            

            


randomgame()



