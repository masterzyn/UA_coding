#!  /usr/bin/env python3

# Importing random module in order to make random numbers
import random

# Getting our random number that the user will try to guess
def get_ran_num():
    return(random.randint(1,100))

def start_game(random_number):

    user_guess = int(input("Guess a number 1-100: "))

    if user_guess > random_number:
        print("Too high.")
        continue_game(random_number)
    elif user_guess < random_number:
        print("Too low.")
        continue_game(random_number)
    else:
        print("You got it right!")
        cont = input("Play again? (y/n): ")
        if cont == "y":
            start_game(get_ran_num())
        else:
            exit()


def continue_game(random_number):
    user_guess = int(input("Guess a number 1-100: "))

    if user_guess > random_number:
        print("Too high.")
        continue_game(random_number)
    elif user_guess < random_number:
        print("Too low.")
        continue_game(random_number)
    else:
        print("You got it right!")
        cont = input("Play again? (y/n): ")
        if cont == "y":
            start_game(get_ran_num())
        else:
            exit()   

start_game(get_ran_num())
