def handle_zodiac(year):
    zodiac = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"]
    result = zodiac[year % 12]
    print(f"Your zodiac is {result}.")
    return result


def handle_input():
    try:
        val = input("Enter year: ")
        MIN = 1000
        max = 3000
        if MIN <= int(val) <= max:
            YEAR = int(val)
            handle_zodiac(YEAR)
        else:
            raise ValueError
    except ValueError:
        print(f"Invalid input. \r\nPlease enter a valid year. \r\ne.g. '1990'.")


handle_input()
