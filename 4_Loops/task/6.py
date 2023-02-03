# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 23:32:19 2023

@author: sparrow
"""

usrinput = input("Enter value 1: ")
usrinput2 = input("Enter value 2: ")

while usrinput != "" and usrinput != "":
    value1 = float(usrinput)
    value2 = float(usrinput2)
    
    avg = str((value1+value2) / 2).format(2)
    low = min(value1, value2)
    high = max(value1, value2)
    dist = high - low
    break
    
print(f"\naverage: {avg}\nlow: {low}\nhigh: {high}\ndistance: {dist}".format(avg, low, high, dist))
    
    