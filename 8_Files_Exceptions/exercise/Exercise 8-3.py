def main():
    filename = input("Enter file to open: ")

    file = open(filename, "r")

    sumColumn1 = 0
    sumColumn2 = 0

    for line in file:
        line = line.split()
        
        sumColumn1 += float(line[0])
        sumColumn2 += float(line[1])
        
        # try:
        #     sumColumn1 += float(line[0])
        #     sumColumn2 += float(line[1])
        # except TypeError:
        #     print("Error: File doesn't contain numbers!")
        #     break

    file.close()
    print("Sum of column 1:", sumColumn1)
    print("Sum of column 2:", sumColumn2)
    
main()