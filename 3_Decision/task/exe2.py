#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:28:11 2023

@author: rinseo
"""

"""
    2
"""
# 1. validate input between 1-10
# 2. if input < 1 print < 1, if input > 10 print > 10
# 3. else print the input value

def task2():
    
    try:
        
        userinput = int(input("Enter 5 integer in range 1-10: "))
        
        if userinput < 1:
            print("The number you entered is < 1 \n")
        elif userinput > 10:
            print("The number you entered is > 10 \n")
        else:
            print("You entered %d" %userinput)
    except ValueError:
        print("Input is not a vailid integer \n")
        
task2()