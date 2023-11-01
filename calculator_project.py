#!  /usr/bin/env python3

# Making global vars for the user inputs
num1 = 0
num2 = 0
operation = ''

# Starting by making all of the calculator functions (addition, subtracton, multiplication)

# Addition function
def add(x, y):
    return float(x + y)

# Subtraction function
def minus(x, y):
    return float(x - y)

# Multiplication function
def mult(x, y):
    return float(x * y)

# Division function
def div(x, y):
    return float(x / y)

# Function to get all user inputs
def user_input():
    # Getting user input for first number
    num1 = float(input("Enter your first number: "))
    # Getting user input for second number
    num2 = float(input("Enter your second number: "))
    # Getting user input for an opperation to do do on the numbers
    operation = input("Enter an opperation (+, -, *, /): ")

    # Making a list of valid operators to make sure the user entered a valid one
    valid_operators = ["+", "-", "/", "*"]

    # Checks to see if the user has entered a valid operator
    while operation not in valid_operators:
        # If the user didn't enter a valid operator we ask until they do enter one
        operation = input("Enter a valid opperation please (+, -, *, /): ")
    # Return a touple with both numbers and the chosen operation
    return num1, num2, operation

# This function checks what operation was entered and returns the calculation
def calculator(touple):
# The touple input that we get is in the order num1 [0], num2 [1], operation [2]
    # If + we add and print answer
    if(touple[2] ==  "+"):
        print(add(touple[0], touple[1]))
    # If - we substact and print answer
    elif(touple[2] == "-"):
        print(minus(touple[0], touple[1]))
    # If * we multiply and print answer
    elif(touple[2] == "*"):
        print(mult(touple[0], touple[1]))
    # Else then we divide and print the answer
    else:
        print(div(touple[0], touple[1]))

# Defining a empty string to initilize the continuation question
cont_question = ''

# Loop in order to keep the calculator runnning until the user inputs "q"
while "q" not in cont_question:
    # Gets the users input and puts that input into the calculator function
    calculator(user_input())
    # Asks the user if they want to enter a new question or if they want to quit the program
    cont_question = input('Enter to do a new question / Enter q to quit: ')