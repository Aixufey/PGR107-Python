input = input("Enter input: ")


def printNeat(value):
    n = len(value)
    print("-" * (n + 4))
    print("|" + input + "|")
    print("-" * (n + 4))


printNeat(input)
