"""
    1. Read input from user, should be the name of the month.
    2. Read input from user as days ranging 1 - 31 within a month.
    3. Display the season + the date. e.g. Summer June 21

    First day of Spring is March 20 until June 20
    First day of Summer is June 21 until September 21
    First day of Autumn is September 22 until December 20
    First day of Winter is December 21 until March 19
"""


def handle_season(M, D):
    equinox = [
        {"Spring": {"march": range(20, 31), "april": range(1, 30), "may": range(1, 31)}},
        {"Summer": {"june": range(21, 30), "july": range(1, 31), "august": range(1, 31)}},
        {"Autumn": {"september": range(22, 30), "october": range(1, 31), "november": range(1, 30)}},
        {"Winter": {"december": range(21, 31), "january": range(1, 31), "february": range(1, 28)}}
    ]

    # 4 Objects in the dictionary
    for ele in equinox:
        # Each Object is a key-value pair, whereas season is the key e.g. "Spring"
        # months refers to the value, which is nested Object that contains the season's months e.g. "march 20-31"
        for season, months in ele.items():
            # if input month is in the season's months
            # and dates are within the range of the season's months
            if M in months and D in months[M]:
                print(f"{season} {M.capitalize()} {D}")
    else:
        print(f"'{M}' is not a valid month. Please enter e.g. 'january'.")
    return None


def handle_input():
    try:
        M = input("Enter month of the year: ")
        D = input("Enter day of the month: ")
        MIN = 1
        MAX = 31
        if MIN <= int(D) <= MAX and M != "":
            MONTH = M.strip().lower()
            DAY = int(D)
            handle_season(MONTH, DAY)
        else:
            raise ValueError
    except ValueError:
        print(f"Invalid input. \r\nPlease enter a number between 1 and 31. \r\ne.g. 'march' and '21'.")


handle_input()
