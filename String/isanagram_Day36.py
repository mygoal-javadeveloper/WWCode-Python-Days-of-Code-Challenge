# Write a Python program to check if two strings are anagrams

import re

def is_anagram(str1, str2):
    tempstr1 = ''.join(re.sub(r'\W+','', str1).lower().strip().split())
    tempstr2 = ''.join(re.sub(r'\W+', '', str2).lower().strip().split())
    if sorted(tempstr1) == sorted(tempstr2):
        print(str1, 'and', str2, 'are anagrams')
    else:
        print(str1, 'and', str2, 'are not anagrams')


is_anagram('debit card', 'bad credit')
is_anagram('credit card', 'bad credit')
is_anagram('Eleven plus two', 'Twelve plus one')
is_anagram('Eleven plus one', 'Twelve plus two')
is_anagram('A decimal point', 'I’m a dot in place')
is_anagram('Vacation time', 'I am not active')
is_anagram('Tom Marvolo Riddle', 'I am Lord Voldemort')
is_anagram('listen', 'silent')
is_anagram('heart', 'earth')
is_anagram('10 reeds', '10 deers')