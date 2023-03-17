def integerPower():
    try:
        base = input("Enter base: ")
        pwr = input("Enter exponent: ")
        x = int(base)
        y = int(pwr)
    except ValueError:
        print("Parsing error", end=' ')
    else:
        if y == x:
            return x
        else:
            return pow(x, y)

result = integerPower()
print(result)
