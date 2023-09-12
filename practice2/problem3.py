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
    return (abs((1 / math.tan(math.radians(y))) + 6))**(1/3) + math.sqrt(((x + 1)**3) / (4*y - 2*z))

print("2) Output where x = 1, y = 4, z = 3 is", function2(1, 4, 3)) 

#Task3

def function3(x, y):
    return (5*x*y) / (x**3 - 4) + math.exp(x**2) + math.sqrt( (math.cos(math.radians(y))**2 - y**2) )

print("3) Output where x = 3, y = 0.2 is", function3(3, 0.2))

#Task4

def function4(x, y):
    return math.sqrt(abs(y)) + ( (1/ math.atan(math.log(x))) )  / (x**y - y + 1)

print("4) Output where x = 3, y = 5 is", function4(3, 5))

print()
print("#################################################")
print()
#Task5 

def function5(x, y, z):
    return 4**(x*y) - x**(y*z) + (x*y)**z

print("1) Output where x = 3, y = 1, z = 2 is", function5(3, 1, 2))

#Task6

def function6(x, y, z):
    return (4 * abs(x) - x*y*(z**2)) / (x + math.exp(y*x) - 2*y*z)

print("2) Output where x = 2, y = 2, z = 1 is", function6(2, 2, 1))

#Task7

def function7(x, y, z):
    return ((1 - x + 1 / math.atan(x - 7*y)) / (4*x*z-math.log(y)**2))**(1/5)

print("3) Output where x = 0.8, y = 0.1, z = 4 is", function7(0.8, 0.1, 4))

#Task8

def function8(x, y, z):
    return (2*3*4) / (math.sin(math.radians(x))**3 + math.tan(math.radians(y))**3) - math.sqrt(z**(x-y))

print("4) Output where x = 3, y = 1, z = 3 is", function8(3, 1, 3))

print()
print("#################################################")
print()

#Task9

def function9(x):
    return ((math.log((x - 3)))**4 + 2**x * math.sin(math.radians(3*x))**2) / (4*x - 5.2)

print("1) Output where x = 4 is", function9(int(4)))

#Task10

def function10(x, y, z):
    return math.sqrt(0.6 * x*y*z) + (y ** x)**2 - math.exp(math.sin(math.radians(2*x*x)))

print("2) Output where x = 2, y = 2, z = 1 is", function10(2, 2, 1))

#Task11

def function11(x, y):
    return (math.asin(x**3) - 6) / (8 * (math.cos(math.radians(4*y)) - math.sin(math.radians(4*x))))

print("3) Output where x = 0.5, y = 2 is", function11(0.5, 2))

#Task12

def function12(x, y, z):
    return (abs(math.log(x**3)) + math.exp(2*x)) / (x + 3.4) - 1 / (math.tan(math.radians(3 / (x*y*z)))**3)

print("4) Output where x = 2, y = 1, z = 3 is", function12(2, 1, 3))

