# Create a function that checks if a number is a perfect square

def issquares(num:int) -> bool:
    return (num ** 0.5).is_integer()


try:
    num = int(input("Enter the squares: \n").strip())
    print("Is the given number a perfect squares?:", issquares(num))
except:
    print('Invalid input.')