"""
    the number of unique char in a string using dictionary

"""

string = input("Enter a string: ")

characters = {}

# print true for character that is unique. Making it very simple to find duplicates
for char in string:
    characters[char] = True

print(characters)

print("That string contained", len(characters), "unique characters.")
