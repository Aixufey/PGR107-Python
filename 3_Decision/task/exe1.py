#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:02:51 2023

@author: rinseo
"""

"""
    1
"""

# a 
# print(m) // m = -1
n = 1
m = -1
if n < -m:
    print(n)
else:
    print(m)

# b
# print(n) // n = 1
if -n >= m:
    print(n)
else:
    print(m)

# c
# print(y) // y = 1.0
x = 0.0
y = 1.0
if abs(x - y) < 1:
    print(x)
else:
    print(y)
    
# d
# print(y) // y = 2.0
import math
a = math.sqrt(2.0)
b = 2.0
if a * a == y:
    print(a)
else:
    print(b)

