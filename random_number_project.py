#!  /usr/bin/env python3

# Importing random module in order to make random numbers
import random

# Making random number function to be called when starting a game
def get_ran_num():
    return(random.randint(1,100))

# This is our start game function which takes an input which is our random number that the user guesses
def start_game(random_number):

    # Getting the user input to compair to the random number we input into the start game function
    user_guess = int(input("Guess a number 1-100: "))

    # Checking if the user number is higher than the random number
    if user_guess > random_number:
        # If it is then print too high and continue the game through the start_game function
        print("Too high.")
        start_game(random_number)
    # Checking if the user number is lower than the random number
    elif user_guess < random_number:
        # If it is then print too high and continue the game through the start_game function
        print("Too low.")
        start_game(random_number)
    # Else the numbers are the same
    else:
        # Print that the user got it right and ask if they want to play again
        print("You got it right!")
        cont = input("Play again? (y/n): ")
        # If user wants to play again then we call the start_game function and get a new random number to guess
        if cont == "y":
            start_game(get_ran_num())
        # Else user wants to stop, and the code is stoped
        else:
            exit() 

# Starts the game initally
start_game(get_ran_num())
