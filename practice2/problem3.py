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

def function2(x, y, z):
    return (abs((1 / math.tan(y)) + 6))**(1/3) + math.sqrt(((x + 1)**3) / (4*y - 2*z))

print("2) Output where x = 1, y = 4, z = 3 is", function2(1, 4, 3)) 
