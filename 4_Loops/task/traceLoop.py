#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:36:14 2023

@author: rinseo
"""

n = 1729
total = 0
while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10
    
    
#  digit = 9
#  total = 0 + 9
#  n     = 172
