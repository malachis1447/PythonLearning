# MadLibs.py 
# Kain M. Snyder
# Fri Aug 11th 2023 0304 MDT

# A quick 2-Line MadLibs example to test variables, strings, user input, and concatenation

def MadLibs():

    print("Hello my fellow [PLURAL NOUN]'s in 2022. It's me, George Washington, the first [OCCUPATION].")
    PluralNoun1 = input("Enter a plural noun: ")
    Occupation1 = input("Enter an occupation: ")
    print("I have been hiding at [PLACE], where I have been living for the past [NUMBER] of years in secret.")
    Place1 = str(input("Enter a Place: "))
    Num1 = int(input("Enter a Number: "))

    print("Hello my fellow " + PluralNoun1 + "'s in 2022. It's me, George Washington, the first " + Occupation1 + ".")
    print(" I have been hiding at " + Place1 + ", where I have been living for the past" + str(Num1) + "years in secret.")

MadLibs()