
# Open from folder
infile = open("resources/names.txt", "r")

for line in infile:
    line = line.rstrip()
    # Remove specific characters from Right side
    line = line.rstrip(".?")
    # Remove specific character from Left side
    line = line.lstrip("!")
    # Remove a sequence of characters somewhere
    line = line.strip("---")

    # Split words in tokens and loop over the words
    word_list = line.split()
    for word in word_list:
        print(word)

    # Split using regex
    sublist = line.split(":")
    for w in sublist:
        print(w, end=" ")

infile.close()
