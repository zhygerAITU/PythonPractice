#Practie 2, problem 2 (Independent Work)

import math

def solve(x, y):

    H = math.sqrt(math.cos(2*y) + math.sin(4*y) + math.sqrt(math.exp(x) - math.exp(-x)))
    H = H / ( (math.exp(-x) + math.exp(x))**3 * ((math.sin(4*y) + math.cos(2*y) - 2)**2)  )

    print(H)

x = int(input("x variable: "))
y = int(input("y variable: "))

solve(x, y)