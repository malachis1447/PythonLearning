# AdvancedCalculator.py
# Kain M. Snyder
# Fri Aug 11th 0410 MDT

from math import *
import logging

def OperatorSelection():
    print("Please select using the numbers in the list which operation you'd like to perform: ")
    print("\n [1]: Addition \n [2]: Subtraction \n [3]: Multiplication \n [4]: Division \n [5]: Exponent \n [6]: Square Root \n \n [0]: Exit \n")

    try:

        global Num1
        global Num2
        global Answer
        Operator = int(input("Please enter the operation you'd like to perform (use shortcuts)"))
        Num1 = float(input("Please enter the base number for the equation: "))
        Num2 = float(input("Please enter the secondary number in the equation, or zero for none: "))
        
    except ValueError:
        logging.error("This program only accepts numbers, please try again")
        OperatorSelection()

    try:

        if Operator == 1:
            AdditionFunc()
        elif Operator == 2:
            SubtractionFunc()
        elif Operator == 3:
            MultiplicationFunc()
        elif Operator == 4:
            DivisionFunc()
        elif Operator == 5:
            ExponentFunc()
        elif Operator == 6:
            SqrtFunc()
        elif Operator == 0:
            quit()
        else:
            print("Your input was not recognized. Please try again.")
            OperatorSelection()

    except ValueError:
        logging.error("This program only accepts numbers, please try again.")
        OperatorSelection()

def AdditionFunc():
    print("The sum is: " + str(Num1 + Num2))
    OperatorSelection()

def SubtractionFunc():
    print("The answer is: " + str(Num1 - Num2))
    OperatorSelection()

def MultiplicationFunc():
    print("The answer is: " + str(Num1 * Num2))
    OperatorSelection()

def DivisionFunc():
    try:
        print("The answer is: " + (Num1 / Num2))
    except ZeroDivisionError:
        logging.error(" Division by zero isn't possible")
        OperatorSelection()

def ExponentFunc():
    print("The exponent's value is: " + (Num1 ** Num2))
    OperatorSelection()

def SqrtFunc():
    print("The square root of " + str(Num1) + " is: " + str(sqrt(Num1)))
    OperatorSelection()

OperatorSelection()