# Create a program that swaps the values of two variables.

def swap_twovariablesval(var_a, var_b):
    var_a, var_b  = var_b, var_a
    return var_a, var_b

var_a = input()
var_b = input()
print('Intial var_a value:', var_a, 'and var_b value:', var_b)
var_a, var_b = swap_twovariablesval(var_a, var_b)
print('After swapping var_a value:', var_a, 'and var_b value:', var_b)
