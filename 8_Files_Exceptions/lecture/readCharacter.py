

infile = open("resources/char.txt")

# Read only 7 characters
char = infile.read(7)
print("Read 7 chars: ",char)

# Returning a list of lines, including also line separator i.e. \n
lines = infile.readlines()
print("Lines in a list: ", lines)


