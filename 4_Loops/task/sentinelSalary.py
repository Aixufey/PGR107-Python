#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:50:25 2023

@author: rinseo
"""


# total = 0.0
# value = float(input("Enter number: "))

# while value >= 0.0:
    
#     toFloat = float(value)
#     total = total + toFloat  
#     print(toFloat)
#     value = input("Enter number: ")



total = 0
count = 0


salary = float(input("Enter salary or -1 to finish: "))

while salary >= 0.0:
    total = total + salary
    count = count + 1
    salary = float(input("Enter salary or -1 to finish: "))


if count > 0:
    avg = total / count
    print("Average salary is %.1f" % avg)
else:
    print("Not valid input")