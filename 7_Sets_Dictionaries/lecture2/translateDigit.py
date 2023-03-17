def main():
    digits = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
        '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }

    phone_number = input("Enter your phone number: ")

    result = translate(digits, phone_number)

    print("Your phone number is: ", result)


def translate(digits, phone_number):
    result = ""
    for char in phone_number:
        result += digits.get(char, "_") + " "
    return result


main()
