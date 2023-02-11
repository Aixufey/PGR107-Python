"""
    Random number and simulations
"""
from random import *

for i in range(10):
    number = random()
    print("%.2f" % number, end=' ')
print()

# Generating an integer
for i in range(10):
    randomInt = randint(-10, 1)
    print("%d " % randomInt, end=' ')
print()

for i in range(10):
    numFloat = uniform(-10, 10)
    print("%.2f" % numFloat, end=' ')
print()

