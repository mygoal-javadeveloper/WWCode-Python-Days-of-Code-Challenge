# Create a function that returns the key with the maximum value in a dictionary

def findmaxvalkey(mydict:dict):
    return [key for key, val in mydict.items() if val == max(mydict.values())][0]

def findmaxvalkey_sorted(mydict:dict):
    mydict = sorted(mydict.items(), key=lambda x:x[1], reverse = True)
    return mydict[0][0]

def findmaxvalkey_max(mydict:dict):
    return max(mydict, key=mydict.get)


mydict = {'A': 5, 'B':1, 'C':121, 'D':10, 'E':21}
print('The key with max value in the given dictionary is:', findmaxvalkey(mydict))
print('The key with max value in the given dictionary is:', findmaxvalkey_sorted(mydict))
print('The key with max value in the given dictionary is:', findmaxvalkey_max(mydict))
