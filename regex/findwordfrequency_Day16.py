# Write a function that counts the frequency of each word in a sentence.

import re
from collections import Counter

def findwordsfrequency(sentence):
    sentence = sentence.lower().strip()
    cleantxt = re.sub(r'[^\w\s]', '', sentence).strip().split()
    for key, val in Counter(cleantxt).items():
        if val > 1:
            print(f"The word '{key}' occurs {val} times in the sentence.")
        else:
            print(f"The word '{key}' occurs {val} time in the sentence.")



sentence = input('Enter the sentence: \n')
findwordsfrequency(sentence)
