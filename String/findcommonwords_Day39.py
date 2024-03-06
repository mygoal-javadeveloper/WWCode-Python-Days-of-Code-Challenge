# Write a program to find the most common words in a text file

import re
from collections import Counter
def findmostcommonwords():
    text = open('textfile.txt', 'r').read().lower().strip()
    # text =  open('anothertextfiles.txt', 'r', encoding='utf-8').read().lower().strip()
    # cleantxt = re.sub(r'\W+', ' ', text).lower().strip().split(' ')
    # cleantxt = re.sub(r'[^\w\s]', '', str)
    cleantxt = re.findall(r'[a-z]+', text)
    print(cleantxt)
    mostfreqwords = Counter(cleantxt).most_common(5)
    print(mostfreqwords)


findmostcommonwords()