from random import *


def main():
    NUM_THROWS = 10000
    rolls = {
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0
    }
    """
        we call also make an empty dictionary and loop
        
        counts = {}
        for i in range(2, 13):
            rolls[i] = 0
    """

    for i in range(NUM_THROWS):
        t = twoDice()
        rolls[t] += 1

    print("Total\t\tSimulated")
    print("-" * 20)

    for i in rolls:
        print("%5d %12.2f" % (i, rolls[i] / NUM_THROWS * 100))


def twoDice():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1 + dice2


main()
