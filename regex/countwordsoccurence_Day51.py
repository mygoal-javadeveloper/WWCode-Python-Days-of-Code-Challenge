# Create a program that counts the occurrences of each word in a text file

import re
from collections import Counter

def count_wordoccurence(filename:str):
    text = open(filename, 'r').read().lower().strip()
    clean_text = re.findall(r'[a-z]+', text)
    for key, val in Counter(clean_text).items():
        if val > 1:
            print(f"The word '{key}' occurs {val} times in the sentence.")
        else:
            print(f"The word '{key}' occurs {val} time in the sentence.")

count_wordoccurence('textfile.txt')