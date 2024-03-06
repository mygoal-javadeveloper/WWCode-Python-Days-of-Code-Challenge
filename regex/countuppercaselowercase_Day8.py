# Write a function that accepts a string and calculates the number of uppercase and lowercase
# letters in it.

import re
def countupperlowercase(mystr:str) -> tuple:
    uppercase = len(re.findall(r'[A-Z]', mystr))
    lowercase = len(re.findall(r'[a-z]', mystr))
    return uppercase, lowercase


def countupperlowercase1(mystr:str) -> tuple:
    uppercase = len(list(filter(lambda letter: letter.isupper(), mystr)))
    lowercase = len(list(filter(lambda letter: letter.islower(), mystr)))
    return uppercase, lowercase


mystr = input('Enter the text: \n')
uppercase, lowercase = countupperlowercase(mystr)
print(f'There are total {uppercase} uppercase letters and {lowercase} lowercase letters in the given text.')
uppercase, lowercase = countupperlowercase1(mystr)
print(f'There are total {uppercase} uppercase letters and {lowercase} lowercase letters in the given text.')

# There are 10 Ships Sailing in Blue Sea.