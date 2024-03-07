# Create a program to calculate the area of a circle given its radius.

from math import pi

def getcirclearea(radius:float) -> float:
    return round((pi * radius**2), 2)

try:
    radius = input('Enter the radius of the circle: \n').strip().strip()
    radius = float(radius)
    if radius > 0:
        print(f'The area of the circle with radius {radius} is {getcirclearea(radius)}')
    else:
        print('Radius of the circle should be positive')
except:
    print('Invalid input')