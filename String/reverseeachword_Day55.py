# Create a function that takes a string and returns the reverse of each word

def reverse_each_words_in_string(mystr: str) -> str:
    return mystr[::-1]


mystr = input('Enter a sentence: \n').strip()
print(reverse_each_words_in_string(mystr))