# Create a program that checks if a given string is a valid email address

from email_validator import validate_email, EmailNotValidError

def isvalidemail(email):
    try:
        print('The given email:', email, 'is:', str(validate_email(email, check_deliverability=True)).replace('<', '').strip().split(' ')[0])
    except EmailNotValidError as eve:
        print(str(eve))


email = input('Enter your email: \n')
isvalidemail(email)