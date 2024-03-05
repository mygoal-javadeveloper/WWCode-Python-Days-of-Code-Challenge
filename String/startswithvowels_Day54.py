# Create a function to find all words in a sentence that start with a vowel

import re
def words_startswithvowels(mystr: str):
    templst = mystr.split()
    for word in templst:
        if word.lower().startswith(('a','e','i','o', 'u')):
            word = re.sub(r'[^\w\s]', '',word)
            print(f"The \"{word}\" in the given sentence starts with \"{word[0].lower()}\" vowel alphabet.")


mystr = input("Enter a sentence: \n").strip()
words_startswithvowels(mystr)