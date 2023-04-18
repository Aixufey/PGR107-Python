"""
    File reader
"""

"""
    Reader
    Everything returned is considered as "string" by readline()
    Parsing digits using float method
"""
infile = open("sample.txt", "r")

line = infile.readline()
while line != "":
    print(line, end="")
    line = infile.readline()

infile.close()


"""
    Writer
"""

outfile = open("sample2.txt", "w")

outfile.write("Welcome to PGR107.\n")
outfile.write("This is another line.\n")
outfile.close()


