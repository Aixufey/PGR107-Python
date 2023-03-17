"""
    Read input from user.
    If the input contains 'a,e,i,o,u' then display it's a vowel.
    Edge case: If input only is 'y' then display it can be a vowel and consonant.
    Otherwise, display it's a consonant.
"""


def handleCount(word):
    counter = 0
    for i, vowel in enumerate(word):
        if vowel in 'aeiouAEIOU':
            counter += 1
    return counter


def handleInput():
    val = input("Enter a word:")
    n = handleCount(val)
    con = handleConsontant(val)
    isVowel = val

    if con != "" and con is not None:
        print(con)

    for i in 'aeiouAEIOU':
        isVowel = isVowel.replace(i, "_")
    print(f"There is {str(n)} vowel{'s' if n != 1 else ''} in {isVowel}.")


def handleConsontant(word):
    if len(word) == 1 and word in 'yY':
        return "Y is a vowel or a consonant."
    elif 'y' in word.lower():
        return "Y is consonant."
    else:
        return ""


handleInput()
