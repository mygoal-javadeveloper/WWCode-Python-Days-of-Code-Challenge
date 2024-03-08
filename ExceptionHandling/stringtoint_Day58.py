# Create a function that converts a string to an integer and handles ValueError

def userinput():
    try:
        num = int(input('Enter an integer: \n').strip())
    except ValueError as ve:
        print('Invalid Input:', ve)
    else:
        print('The given integer value is:', num)


userinput()