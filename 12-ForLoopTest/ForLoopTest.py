# ForLoopTest.py 
# Kain M. Snyder
# Wed August 23rd 2023 0024 MDT
# Print an array, one value at a time using a For Loop

def FriendsLoop():
    Friends = ["Brandon", "Jerry", "Aubrey"]
    for Friend in Friends:
        print(Friend)
    IndexInRange()

def IndexInRange():
    for Index in range(69, 79):
        if Index == 69 or Index == 78:
            print("Nice")
        else: 
            print("Not Nice")

FriendsLoop()