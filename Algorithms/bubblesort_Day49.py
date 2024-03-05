# Create a program that implements the bubble sort algorithm

def bubblesortalgorithm(lst):
    # sorting in ascending order
    for idx in range(len(lst)):
        no_swap = True
        for idxa in range(0, len(lst)-idx-1):
            if lst[idxa] > lst[idxa+1]:
                lst[idxa], lst[idxa+1] = lst[idxa+1], lst[idxa]
                no_swap = False
        if no_swap:
            return lst
    return lst
try:
    lst = list(map(int, input('Enter the element of the list separated by space: \n').strip().split()))
    print(bubblesortalgorithm(lst))
except:
    print('Invalid input.')



