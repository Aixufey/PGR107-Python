"""
    4. Read user input and print the string in reverse.
"""

userinput = input("Enter a word: ")
def reverseInput(string):
    reversed = ""
    # For each character in the string do..
    for char in string:
        # previous value = current character inside loop index _
        reversed = char + reversed
    return reversed

result = reverseInput(userinput)
print(result)

"""
    start: The index of the first character in the slice (default is 0).
    end: The index of the first character that is NOT in the slice (default is the length of the string).
    step: The number of indices between slice elements (default is 1).
    
    s = "Hello, World!"
    s[7:12]  # returns "World"
    s[:5]    # returns "Hello"
    s[7:]    # returns "World!"
    s[::2]   # returns "Hlo ol!"
"""
def reversedEnhanced(string):
    reversed = string[::-1] # is like string[0,0,-1]
    print(reversed)
reversedEnhanced(userinput)

"""
    So the slicing will start from the end of string. 
    start and end is not specified the default is `0`
    But the step is `-1`, this means the slice will returning all characters from tail -> head = reversed

"""