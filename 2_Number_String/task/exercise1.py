#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:35:49 2023

@author: rinseo
"""
"""
    String formatter
    %s - string
    %d - integer
    %f - float
"""
quantity = 24
total = 17.289
# %10.2 means make 10 whitespace and justify right
print("Quantity: %d Total: %10.2f" %(quantity, total))

# New way of formatting String
print(f"Quantity {quantity}, total {total}")

"""
    1
"""
x = 2.5 
y = -1.5 
m = 18 
n = 4

# a
a1 = x + n * y - (x + n) * y
print("a: %s" %a1)

# b
b1 = m // n + m % n #the floor division // rounds the result down to the nearest whole number
print("b: %s" %b1)

# c
c1 = 5 * x -n / 5
print("c: %s, " %c1)

# d
d1 = 1-(1-(1-(1-(1-n))))
print("d: %s" %d1)

# e
import math
squareRoot = math.sqrt( math.sqrt(n) )
print("e %s"%squareRoot)

"""
    2
"""

n2 = 17
m2 = 18

# a
a2 = n // 10 + n % 10
print("a2: %s" %a2)

# b
b2 = n %2 +m % 2
print("b2: %s" %b2)

# c
c2 = (m + n) // 2
print("c2: %s" %c2)

# d
d2 = (m + n) / 2.0
print("d2: %s" %d2)

# e
e2 = int(0.5 * (m + n))
print("e2: %s" %e2)

# f
f2 = int( round(0.5 * (m + n)))
print("f2: %s" %f2)


"""
    3
"""
s = "Hello"
t = "World"

a3 = len(s) + len(t)
print("a3: %s" %a3)

b3 = s[1] + s[2]
print("b3: %s" %b3)

c3 = s[len (s) // 2]
print("c3: %s" %c3)

d3 = s + t
print(d3)

e3 = t + s
print(e3)

f3 = s * 2
print(f3)


"""
    4
"""

# Program to prompt a user for two inputs
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

theSum = number1 + number2
print("Sum = %17d" %theSum)

theDiff = number1 - number2
print("Difference = %10d " %theDiff)

theProd = number1 * number2
print("Product = %13d" %theProd)

theAvg = (number1 + number2) / 2
print("Average = %13.2f" %theAvg)

theDistance = math.dist([number1], [number2])
print("Distance = %12d" %theDistance)

theMax = max(int(number1), int(number2))
print("Maximum = %13d" %theMax)

theMin = min(int(number1), int(number2))
print("Minimum = %13d" %theMin)