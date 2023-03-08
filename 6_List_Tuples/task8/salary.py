"""
    If hours less than 40, Rate = 8.00$ per hour
    Otherwise, + 320$ AND Rate = 12.00$ per hour

    Algorithm:
    1. Ask user to enter hours
    2. If hours < 40, Rate = 8.00
    3. Otherwise, Rate = 12.00 AND + 320 additional
    4. Print salary
"""


def handle_salary(hours):
    rate = 0
    total = 0
    if hours < 40:
        rate = 8.00
        total = hours * rate
    else:
        rate = 12.00
        total = "{:.2f}".format((hours * rate) + 320)
    print(f"Rate {rate}/ hour - your salary is {total}$")


def handle_input():
    try:
        hours = float(input("Enter hours: "))
        if hours > 0:
            handle_salary(hours)
        else:
            raise ValueError
    except ValueError:
        print(f"Invalid input.\r\nPlease enter a valid number.")


handle_input()