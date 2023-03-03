"""
    1. A month can be 28 to 31 days.
    2. Read input from user to evaluate days of the month.
    3. Display the days of the month if exists.
    Edge case: February in a Leap Year contains 29 days.

    Leap Year rules
    Year must be divisible by 4, no decimals
    If a century year, must be divisible by 100 and 400

    Thirty days have September,
    April June and November.
    When short february's done,
    All the rest have thirty-one.
"""


def handle_days(Y, M):
    end_of_century = str(Y)[2:] == "00"
    leap_year = Y % 4 == 0 and (Y % 100 != 0 or Y % 400 == 0)
    months = [
        {'january': 31}, {'february': 29 if end_of_century else 28}, {'march': 31}, {'april': 30},
        {'may': 31}, {'june': 30}, {'july': 31}, {'august': 31}, {'september': 30},
        {'october': 31}, {'november': 30}, {'december': 31}
    ]
    for month in months:
        if M.strip().lower() in month:
            print(
                f"{M.capitalize()} in {Y} has {list(month.values())[0]} days, and is {'not ' if not leap_year else ''}a leap year.")
            break
    else:
        print(f"'{M}' is not a valid month.")


def handle_input():
    YEAR = ""
    try:
        YEAR = input("Enter year: ")
        MONTH = input("Enter month: ")
        MIN = 1000
        MAX = 9999
        if YEAR.isdigit() and MIN <= int(YEAR) <= MAX:
            handle_days(int(YEAR), MONTH)
        else:
            raise ValueError
    except ValueError:
        print(f"'{YEAR}' is not a valid input. Please enter a 4-digit year.")


handle_input()
