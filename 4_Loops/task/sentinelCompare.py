#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:41:08 2023

@author: rinseo
"""

value = int(input("Enter a integer: "))
userinput = input("Enter a integer: ")

while userinput != "":
    # left
    prev = value
    # right
    value = int(userinput)
    
    # if left and right is same == dupes
    if value == prev:
        print("Duplicate values in a sequence")
    userinput = input("Enter a integer: ")
    
