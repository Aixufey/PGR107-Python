"""
    Employee Rating
    Scale from 0.0, 0.4, 0.6 or more.
    The amount of raise is 2400.00 * rating.

    Algorithm:
    1. Ask user to enter rating
    2. If rating < 0.0 or rating > 1.0, raise ValueError
    3. If rating < 0.4, print "Unsatisfactory"
    4. If rating < 0.6, print "Satisfactory"
    5. If rating >= 0.6, print "Meritorious"
    6. Print raise
"""


def handle_raise(rating):
    raise_amount = 0
    if rating < 0.4:
        raise_amount = 0
        print("Unsatisfactory")
    elif rating < 0.6:
        raise_amount = 2400.00 * rating
        print("Satisfactory")
    else:
        raise_amount = 2400.00 * rating
        print("Meritorious")
    print(f"Your raise is {raise_amount}$")


def handle_input():
    try:
        rating = float(input("Enter your rating 0.4, 0.6 or more\r\nEnter: "))
        if 0.0 <= rating <= 1.0:
            handle_raise(rating)
        else:
            raise ValueError
    except ValueError:
        print(f"Invalid input.\r\nPlease enter a valid number. \r\ne.g. '0.4' or '0.6'.")


handle_input()
