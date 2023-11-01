#!  /usr/bin/env python3

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

# Getting user input for first number
num1 = float(input("Enter your first number: "))
# Getting user input for second number
num2 = float(input("Enter your second number: "))
# Getting user input for an opperation to do do on the numbers
opperation = input("Enter an opperation (+, -, *, /): ")

print(num1, num2, opperation)