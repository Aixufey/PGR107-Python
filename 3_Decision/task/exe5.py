#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:16:09 2023

@author: rinseo
"""

"""
    5
"""


def enhancedConverter():
    choice = input("Select 1 - metric \nSelect 2 - imperial \n")
    
    weight = float(input("Enter weight: "))
    
    if choice == "1":
        assert weight > 0
        result = weight * 2.2
        print("Your weight in pounds is '%.2flbs' " % result)
    else:
        result = weight * 0.45
        assert weight > 0
        print("Your weight in kg is '%dkg' " % result)
        
enhancedConverter()
