n = int(input("Input your number: "))

import math

def solve(n):

    return n**2 / 3 + (n**2 + 4) / 6 + math.sqrt(n**2 + 4) / 4 + math.sqrt((n**2 + 4)**3) / 4

print("Answer is:", solve(n))