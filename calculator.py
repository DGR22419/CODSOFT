"""
calculator :-

Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.
"""

print("welcome to calculator . ")


def inputx():
    try :
        x = int(input("enter first number : "))
    except :
        inputx()

def inputy():
    try : 
        y = int(input("enter second number : "))
    except :
        inputy()

inputx()
inputy()

def menu() :
    print("1) addition ")