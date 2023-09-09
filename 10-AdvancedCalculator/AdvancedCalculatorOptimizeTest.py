# AdvancedCalculatorOptimizeTest.py
# Kain M. Snyder
# 05 Sep 2023 0727 MDT

from math import *
import logging

def OperatorSelectionTest():
  print("Please select using the numbers in the list, which operation you would like to perform")
  print("\n [1]: Addition \n [2]: Subtraction \n [3]: Multiplication \n [4]: Division \n [5]: Exponents \n [6]: Square Root \n")

  try: 
    OperatorTest = int(input("Please enter the operation you'd like to perform"))
    Num1 = float(input("Please enter the base number for the equation: "))
    Num2 = float(input("Please enter the secondary number in the equation, or zero for none")) 

  except ValueError: 
    logging.error("This program only accepts numbers, please try again")
    OperatorSelectionTest()

  try: 
    match OperatorTest:
      case 0:
        exit()
      case 1:
        AdditionFuncTest(Num1, Num2)
      case 2:
        SubtractionFuncTest(Num1, Num2)
      case 3:
        MultiplicationFuncTest(Num1, Num2)
      case 4:
        DivisionFuncTest(Num1, Num2)
      case 5:
        ExponentFuncTest(Num1, Num2)
      case 6:
        SqrtFuncTest(Num1)
      case _:
        logging.error("Your input was not recognized, please try again")
        OperatorSelectionTest()
  except ValueError: 
      logging.error("This program only accepts numbers, please try again")
      OperatorSelectionTest()

def AdditionFuncTest(Num1, Num2):
    print("The sum is: " + str(Num1 + Num2))
    OperatorSelectionTest()

def SubtractionFuncTest(Num1, Num2):
    print("The answer is: " + str(Num1 - Num2))
    OperatorSelectionTest()

def MultiplicationFuncTest(Num1, Num2):
    print("The answer is: " + str(Num1 * Num2))
    OperatorSelectionTest()

def DivisionFuncTest(Num1, Num2):
    try:
        print("The answer is: " + str(Num1 / Num2))
    except ZeroDivisionError:
        logging.error(" Division by zero isn't possible")
        OperatorSelectionTest(Num1, Num2)

def ExponentFuncTest(Num1, Num2):
    print("The exponent's value is: " + str(Num1 ** Num2))
    OperatorSelectionTest()

def SqrtFuncTest(Num1):
    print("The square root of " + str(Num1) + " is: " + str(sqrt(Num1)))
    OperatorSelectionTest()

OperatorSelectionTest()
