#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:34:32 2023

@author: rinseo
"""

richter = float(input("Enter the magnitude on the Richter scale: "))

if richter >= 8.0:
    print("Most structures fall")
elif richter >= 7.0:
    print("Many buildings destroyed")
elif richter >= 6.0:
    print("Many buildings considerably damaged")
elif richter >= 4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No destruction to buildings")
    