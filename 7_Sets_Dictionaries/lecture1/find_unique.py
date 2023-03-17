# This is Python. Python is fun. I love Python. Do you like Python?


def clean(string):
    result = ""
    for char in string:
        if char.isalnum():
            result = result + char.lower()
    return result


unique_words = set()

sentence = input("Enter a sentence: ")

the_words = sentence.split()  # list of words

for word in the_words:
    cleaned = clean(word)
    if cleaned != "":
        unique_words.add(word)
        print(word)

print("The sentence contains ", len(unique_words), "unique words.")
