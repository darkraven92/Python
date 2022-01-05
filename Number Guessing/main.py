import random

def compareinput(x, y):
    wrong_guesses = 0
    score = 0
    if x != y:
        print("Wrong")
    else:
        print("Correct")
        
    

def randomgame():

    while True:
        score = 0
        wrong_guesses = 0

        print("Welcome to this Number Guessing Game!\n")

        print("Guess a number between")
        print("1. 1-10")
        print("2. 1-100")
        print("3. Any range")
        print("4. Show score")
        print("5. Quit")

        user_input = input("> ")

        if user_input == "1":
            number = random.randint(1,10)
            user_guess = input("Guess a number between 1-10 ")
            while user_guess != number:
                user_guess = int(input("Wrong! Guess again:  "))
                wrong_guesses += 1
                if wrong_guesses > 3 & wrong_guesses != 4:
                    user_hint = input("Do you want a hint? Yes/No ")
                    if user_hint == "Yes":
                        if(number%2 == 0):
                            print("The number is divisible by 2")
                        else:
                            print("The number is not divisible by 2")
                if wrong_guesses > 5:
                    user_hint2 = input("Do you want another hint? Yes/No ")
                    if user_hint2 == "Yes":
                        if number > 5 & number < 10:
                            print("The number is between 5-10")
                        else:
                            print("The number is between 1-5")
            print("You guessed the correct number!",number)
            score += 1
        
        if user_input == "2":
            number = random.randint(1,100)
            user_guess = input("Guess a number between 1-100: ")
            while user_guess != number:
                compareinput(user_guess, number)


        if user_input == "5":
            print("Quiting the game..")
            break

            


randomgame()



