# WhileLoopTest.py 
# Kain M. Snyder
# Tue Aug 22 2023 2349 MDT


AttemptCount = 0

def main():
    global AttemptCount
    AttemptCount += 1
    PassPhrase = str("Aubrey")
    Guess = str(input("Please enter the passphrase: "))
    while Guess != PassPhrase:
        main()
    else:
        CorrectGuess()

def CorrectGuess():

    print("Congratulations! You guessed the passphrase successfully! It took you " + str(AttemptCount) + " tries.")
    exit()

main()