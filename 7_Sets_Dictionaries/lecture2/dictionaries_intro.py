def main():
    contacts = {
        "Fred": 6235591,
        "Mary": 3841212,
        "Bob": 3841212,
        "Sarah": 2213278
    }
    # Print Fred from dictionary using list access
    if "Fred" in contacts:
        print("Number for Fred is: ", contacts["Fred"])
    else:
        print("Fred is not in my list.")

    #  Print a list of every contact with a given number
    name_list = findNames(contacts, 3841212)
    print("Names for 3841212:", end=" ")
    for name in name_list:
        print(name, end=" ")

    print()

    printAll(contacts)


def findNames(contacts, number):
    name_list = []

    for name in contacts:
        if contacts[name] == number:
            name_list.append(name)
    return name_list


def printAll(contacts):
    print("All names and numbers: ")

    for key in sorted(contacts):
        print("%-10s %d" % (key, contacts[key]))


main()
