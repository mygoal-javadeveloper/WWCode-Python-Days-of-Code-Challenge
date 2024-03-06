# Write a program to reverse a given string.

def reversestring(mystr):
  mystr = mystr.strip().split()
  mystr.reverse()
  # tempA = ''
  # for idx in range(len(str)):
  #   tempA = tempA + ' ' +str[idx]
  return ' '.join(mystr).strip()

def reverse_each_words_in_string(mystr):
  mystr = mystr.strip()
  return mystr[-1::-1]


print(reversestring('I love Python coding'))
print(reversestring(input()))
print(reverse_each_words_in_string('I love Python coding'))
print(reverse_each_words_in_string(input()))