

try:
    infile = open("resources/charr.txt")
    if infile is not None:
        print(infile)
    else:
        print("Invalid")
        raise TypeError
except FileNotFoundError as fileNotFound:
    print(fileNotFound)


