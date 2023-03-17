def count_vowels(string):
    count = 0
    for char in string:
        if char in 'aeiouAEIOU':
            count += 1
    return count


string = input("Enter a string: ")

vowels = count_vowels(string)
print(f"There are {vowels} in '{string}'")

sentence = input("Enter a word: ")


def count_words(string):
    count = 1

    if not string:
        return 0

    for word in string:
        if word == " ":
            count += 1
    return count


result = count_words(sentence)
print(f"There are {result} words in {sentence}.")
