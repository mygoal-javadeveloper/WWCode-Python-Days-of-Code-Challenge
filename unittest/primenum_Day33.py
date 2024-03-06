# Write a test case for a function that checks if a number is prime

def isprime(num):
    if num <= 1:
       return 0
    else:
        for divisor in range(2, int(num**0.5)+1):
            if not num % divisor:
                return 0
        else:
            return 1



print(isprime(5))
print(isprime(53))
print(isprime(97))
print(isprime(1))
print(isprime(10))
print(isprime(88))