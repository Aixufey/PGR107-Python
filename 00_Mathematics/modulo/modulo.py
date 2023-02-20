def modulo():
    try:
        dividend = int(input("Enter divident: "))
        divider = int(input("Enter divider: "))
        minus(dividend, divider)
    except ValueError:
        print("Invalid input.")


def minus(dividend, divider):
    while dividend >= divider:
        if dividend == divider:
            temp = str(dividend / divider)[:1]
            break
        else:
            temp = dividend - divider
            print(f"{dividend} - {divider} = {temp}  ")
            dividend -= divider
    print(f"Remainder is {temp}")
    return dividend


modulo()

"""
    Scenario: Limit the range that we store in a particular variable
    I want a day with number of 10
    We can limit the range to 7 from 0 - 6 by doing 10 % 7
    0 Monday
    1 Tuesday
    2 Wednesday
    3 Thursday
    4 Friday
    5 Saturday
    6 Sunday
"""


def checkDayWithModulo():
    while True:
        choice = input("Select 1 for day of the week:\r\nSelect 2 for days calculation:\r\nEnter: ")
        if choice != "1" and choice != "2":
            print("Not a valid option")
            return None
        try:
            days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
            if choice == "1":
                day_of_the_week = int(input("Enter any number to determine day of the week: "))
                result = day_of_the_week % 7
            else:
                # list comprehension iterating over tuple applying lower for each element
                days_to_lower = [day.lower() for day in days]

                start_day = input(
                    "To determine which day of the week in N days, e.g. wednesday\r\nEnter starting day: ").strip().lower()
                end_day = int(input("Enter total days: "))

                # returning index in tuple for given user input
                day_of_the_week = days_to_lower.index(start_day)

                # tl;dr => Suppose we want to calculate from Monday and determine what day of the week it is in 2 weeks.
                # that is total days = index 0 + 14 days modulo 7 days in a week
                total_days = end_day + day_of_the_week
                result = total_days % 7
            for i in range(len(days)):
                if result == i:
                    # msg = f"\tDay of the week: {days[i]} [{i}]"
                    # print(" " * 5 + "Day of the week: %2s %2s" % (days[i], i))
                    print(f"{' ' * 5}Day of the week: {days[i]:<9} [{i}]")
        except ValueError:
            print("Invalid input")
            continue
        else:
            break


checkDayWithModulo()
