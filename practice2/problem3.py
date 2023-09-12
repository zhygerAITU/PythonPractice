#Practie 2, problem 2 (Independent Work)

import math

# x = int(input("Input X: "))
# y = int(input("Input Y: "))
# z = int(input("Input Z: "))

#Task1 

def function1(x, y):
    return (x**y)**x + x**(x**y) - x**4

print("1) Output where x = 2, y = 1 is", function1(2, 1)) 

#Task2