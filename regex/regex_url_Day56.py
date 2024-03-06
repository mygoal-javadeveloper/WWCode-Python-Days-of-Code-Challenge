# Create a function to extract all URLs from a given text using regular expressions

import re

def extracturl(mystr: str) -> list:
    url_pattern = r"(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?([a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})?"
    url_lst = re.findall(url_pattern, mystr)
    for idx, url in enumerate(url_lst):
        url_lst[idx] = ''.join(url)
    return url_lst


mystr = input('Enter a sentence containing website links: \n').strip()
print(extracturl(mystr))
