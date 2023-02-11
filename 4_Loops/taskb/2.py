"""
    Task 2
"""
# a: Only the uppercase
userinput = input("Enter a word: ")

for i in userinput:
    if i.isupper():
        print(i, end=' ')
print()

# b: Every second letter
for i, value in enumerate(userinput):
    if i % 2 == 0:
        print(value, end='')
print()

# Alternative
for i in range(len(userinput)):
    val = userinput[i]
    if i % 2 == 0:
        print(val, end=' ')
print()

# LoL way
val = userinput[::2]
print(val)

# c: replace vowels with _

vowels = userinput
for i in 'aeiouAEIOU':
    vowels = vowels.replace(i, '_')
print(vowels + "\n")

# d: number of digits in the string
words = userinput
isNum = 0
for char in words:
    if char.isnumeric():
        isNum += 1

print(f"There are {isNum} of", "digit." if isNum <= 1 else "digits")

# e:
counter = 0
for i, vowel in enumerate(userinput):
    if vowel in 'aeiouAEIOU':
        counter = counter + 1
print(f"There are {counter} of","vowel." if counter <= 1 else "vowels.")