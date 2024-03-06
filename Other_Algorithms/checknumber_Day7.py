# Write a program to check if a number is positive, negative, or zero.

def checknumber(num):
    if isinstance(num, (int, float)):
        if num == 0:
            return 'Given Number is zero.'
        elif num > 0:
            return 'Given number is positive.'
        else:
            return 'Given number is negative.'
    else:
        return 'Invalid entry.'


print(checknumber(0))
print(checknumber(5))
print(checknumber(-8))
print(checknumber(4.5))
print(checknumber(-2.8))