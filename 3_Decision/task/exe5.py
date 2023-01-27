#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:16:09 2023

@author: rinseo
"""

"""
    5
"""

def weightConverter():
    choice = int(input("Select 1 - metric: \nSelect 2 - imperial: \n"))
    
    weight = 0
    
    if choice == 1:
        usrinput = int(input("Enter value: "))
        assert usrinput >= 0 and usrinput <= 200
        weight = usrinput * 2.2
        print("Your weight in lb is %2.2flb" %float(weight))
    else:
        usrinput = int(input("Enter value: "))
        assert usrinput >= 0 and usrinput <= 200
        weight = usrinput * 0.45
        print("Your weight in kg is %dkg" %int(weight))
    
weightConverter()