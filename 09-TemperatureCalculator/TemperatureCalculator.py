# TemperatureCalculator.py 
# Kain M. Snyder
# Fri Aug 11th 2023 0337 MDT

# Script to calculate Celsius to Farenheit or vice-versa


def ModeSelection():
    print("Please choose which mode of the Temperature Calculator you would like to use: \n")
    print("\n")
    print("[1]: Celsius to Fahrenheit")
    print("[2]: Fahrenheit to Celsius")
    print("\n")
    Selection = int(input("Please type 1 or 2: "))

    if Selection == 1:
        CentigradetoFahrenheit()
    elif Selection == 2:
        FahrenheittoCelsius()
    elif Selection != 1 or 2:
        print("Your selection wasn't recognized. Plesae try again.")
        ModeSelection()

def CentigradetoFahrenheit():
    CtFC = float(input("Please enter the temperature in Celsius that you would like converted to Fahrenheit: "))
    CtFF = float((CtFC * 9/5) + 32)
    print(CtFF)

def FahrenheittoCelsius():
    FtCF = float(input("Please enter the temperature in Fahrenheit that you would like converted to Celsius: "))
    FtCC = float((FtCF - 32) * 5/9)
    print(FtCC)

ModeSelection()