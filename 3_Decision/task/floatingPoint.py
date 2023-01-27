#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 15:06:22 2023

@author: rinseo
"""

userInput = input("Enter a floating point: ")
if userInput.replace(".", "").isdecimal():
    number = float(userInput)
    print("Floating point is: %.2f" %number)