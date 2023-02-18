def modulo():
    try:
        input1 = input("Enter A: ")
        input2 = input("Enter B: ")
        A = int(input1)
        B = int(input2)
    except ValueError:
        print("Invalid input.")
    else:
        if A and B == 0:
            return None
        if A < B:
            print(f"{A} is already less than {B}.")
        else:
            remainder = A % B
            print(remainder)
            return remainder


modulo()
