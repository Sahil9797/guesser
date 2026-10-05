def GuessANumber():
    import random   # used to generate random numbers

    secretNumber = random.randint(3, 30)
    guessCountLimit = 5

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 3 and 30.")
    print("You have 5 attempts to guess it.")
    print("Type 'quit' at any time to exit the game.")

    while True:
        guessCount = 0
        while guessCount < guessCountLimit:
            guess = input("Enter your guess: ")
            if guess.lower() == "quit":
                print("Thanks for playing! Goodbye!")
                return
            # Check if the input is a number
            if not guess.isdigit():
                print("Please enter a number between 3 and 30, or type 'quit'.")
                continue
            guess = int(guess)
            if guess < 3 or guess > 30:
                print("Your guess must be between 3 and 30.")
                continue
            guessCount += 1
            if guess == secretNumber:
                print("Congratulations! You guessed the secret number!")
                break
            elif guess < secretNumber:
                print("Too low!")
            else:
                print("Too high!")
            print("Attempts left:", guessCountLimit - guessCount)
        else:
            print("Sorry! You used all 6 attempts.")
            print("The secret number was:", secretNumber)
        playAgain = input("Would you like to play again? (yes/no): ")
        if playAgain.lower() != "yes":
            print("Thanks for playing! Goodbye!")
            break
        # Generate a new secret number for the next game
        secretNumber = random.randint(3, 30)

GuessANumber()
