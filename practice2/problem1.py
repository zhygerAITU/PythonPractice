#Practice 2, Problem 1 (Independent work)

import math

def solve(a, b, h):

    return (pow(a, 2) + b) * h / (2 * (a - b) + 4)
    


a = int(input("Input 'a' variable: "))
b = int(input("Input 'b' variable: "))
h = int(input("Input 'h' variable: "))

print("The result is ", solve(a, b, h))
