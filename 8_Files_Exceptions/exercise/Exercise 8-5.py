input_list = []
tries = 2

while tries != 0:
    try:
        inputN = float(input("Enter a number: "))
        input_list.append(inputN)
        
    except ValueError:
        tries -= 1
        if tries != 0:
            print("Not a number! Enter a number to continue")
            print("or enter a character to quit.")

print("Sum =", sum(input_list))