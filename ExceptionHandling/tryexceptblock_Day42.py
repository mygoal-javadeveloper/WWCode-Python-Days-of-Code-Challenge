# Write a program that uses a try-except block to handle division by zero

def division(dividend, divisor):
    try:
        quotient = int(dividend) / int(divisor)
    except ZeroDivisionError as zde:
        print('ZeroDivisionError:', zde)
    except ValueError as ve:
        print('ValueError:', ve)
    except Exception as e:
        print('Exception:', e)
    else:
        print('The quotient of the division is:', quotient)
    finally:
        print('End of division function!')

dividend = input('Enter the dividend: \n')
divisor = input('Enter the divisor: \n')
division(dividend, divisor)
