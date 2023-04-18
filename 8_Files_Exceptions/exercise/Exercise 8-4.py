def main():
    filename = input("File to open: ")
    file = open(filename, "r")
    numCharacters = 0
    numWords = 0
    numLines = 0

    for line in file:
        numCharacters += len(line.strip())
        numWords += len(line.split(" "))
        numLines += 1
    file.close()
    print("Num characters:", numCharacters)
    print("Num words:", numWords)
    print("Num lines:", numLines)

main()