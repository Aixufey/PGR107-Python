#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:01:42 2023

@author: rinseo
"""


"""
    4
"""

def myCalculator():
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    ops = input("Enter operation: ")
    result = 0
    
    if ops != '+' and ops != '-' and ops != '/' and ops != '*':
        print("N/A")
    elif ops == '*':
        result = a * b
    elif ops == '/':
        result = a / b
    elif ops == '+':
        result = a + b
    elif ops == '-':
        result = a - b
    print("Result is %2.2f" %float(result) )
    
myCalculator()