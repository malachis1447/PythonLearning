# AdvancedCalculator.py
# Kain M. Snyder
# Fri Aug 11th 0410 MDT

from math import *

def OperatorSelection():
    print("Please select using the numbers in the list which operation you'd like to perform: ")
    print("\n [1]: Addition \n [2]: Subtraction \n [3]: Multiplication \n [4]: Division \n [5]: Exponent \n [6]: Square Root")

    Operator = int(input("Please type the number of your above selection: "))

    global Num1
    global Num2
    global Answer

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

def AdditionFunc():

    Num1 = float(input("Please enter the first number to add: "))
    Num2 = float(input("Please enter the second number to add: "))

    Answer = Num1 + Num2
    print("The sum is: " + str(Answer))
    OperatorSelection()

def SubtractionFunc():

    Num1 = float(input("Please enter the base number to be subtracted from: "))
    Num2 = float(input("Please enter the number to be subtracted from base: "))

    Answer = Num1 - Num2
    print("The answer is: " + str(Answer)) 
    OperatorSelection()

def MultiplicationFunc():

    Num1 = float(input("Please enter the first number to be multiplied: "))
    Num2 = float(input("Please enter the second number to multiply by: "))

    Answer = Num1 * Num2
    print("The answer is: " + str(Answer))
    OperatorSelection()

def DivisionFunc():

    Num1 = float(input("Please enter the base number to be divided: "))
    Num2 = float(input("Please enter the number for the base to be divided by: "))

    Answer = Num1 / Num2
    print("The quotient is: " + str(Answer))
    OperatorSelection()

def ExponentFunc():
    Num1 = float(input("Please enter the exponent's base number: "))
    Num2 = float(input("Please enter the exponent's power: "))
    Answer = Num1 ** Num2
    print("The exponent's value is: " + str(Answer))
    OperatorSelection()

def SqrtFunc():
    Num1 = float(input("Please enter the Number you'd like the square root of: "))
    Answer = sqrt(Num1)
    print("The square root of " + str(Num1) + " is: " + str(Answer))

OperatorSelection()