#!  /usr/bin/env python3

# Importing random module in order to make random numbers
import random

# Getting our random number that the user will try to guess
random_number = random.randint(1,100)

user_guess = int(input("Guess a number 1-100: "))

if user_guess > random_number:
    print("Too high.")
elif user_guess < random_number:
    print("Too low.")
else:
    print("You got it right!")