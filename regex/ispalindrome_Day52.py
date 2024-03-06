# Create a program that checks if a string is a palindrome

import re
def ispalindrome(mystr: str) -> str:
    mystr = re.sub(r'[\s]', '', mystr).strip().lower()
    if mystr == mystr[::-1]:
        return 'Given string is a palindrome'
    else:
        return 'Given string is not a palindrome'


mystr = input('Enter the string to check if it is a palindrome or not: \n')
print(ispalindrome(mystr))
