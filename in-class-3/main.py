
import math
from random import randint


def program0():
    i = 1

    while i < 100:
        i+= i
    
    print(f'Sum: {i}')

def program1(x):
    output = []
    while x > 0:
        output.append(x % 2)
        x = math.floor(x/2)
      
    for num in output:
        print(num)

def program2():
    val = 1
    bid = input("I'll bid $1!")

    while bid != 'n':
        val += randint(1, val)
        bid = input("I'll bid $" + str(val) + "!")

#program 3
# 1: 0
# 2: 0
# 3: line 4
# 4: 1
# 5: 1
# 6: line 4
# 7: 2
# 8: 