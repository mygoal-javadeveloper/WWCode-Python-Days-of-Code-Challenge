# Create a program that capitalizes the first letter of each word in a sentence
import string

def capitalizeeachwords_1(mystr):
    return mystr.title()


def capitalizeeachwords_2(mystr):
    return string.capwords(mystr)



mystr = input('Enter a sentence: \n')
print(capitalizeeachwords_1(mystr))
print(capitalizeeachwords_2(mystr))