def main():
    openFilename = input("File to open: ")
    saveFilename = input("File to save into: ")

    readFile = open(openFilename, "r")
    writeFile = open(saveFilename, "w")

    lineNumber = 1
    for line in readFile:
        writeFile.write("/* %s */ %s" % (lineNumber, line))
        lineNumber += 1

    readFile.close()
    writeFile.close()
    
main()