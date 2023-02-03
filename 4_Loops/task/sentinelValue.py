#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:42:36 2023

@author: rinseo
"""

## sum of first 100 numbers
## Sentinel value is 100 means when we hit 100 it will have a meausure point

number = 1
total = 0

while number <= 100:
    total += number
    number += 1
    print(total)