# Write a program that reads an integer from the user and handles invalid inputs

def user_input():
    try:
        num = int(input('Enter an integer (a zero or positive or negative whole number without decimals): \n'))
    except ValueError as ve:
        print('ValueError:', ve)
    except Exception as e:
        print('Exception:', e)
    else:
        print(num)

user_input()
