# Write a program to print the first n numbers of a Fibonacci sequence

def fibonacci():
  n = input()
  if n.isdigit():
    a, b = 0, 1
    for x in range(int(n)):
      print(a, end=", ")
      a, b = b, a+b
  else:
    print("Invalid entry")

fibonacci()