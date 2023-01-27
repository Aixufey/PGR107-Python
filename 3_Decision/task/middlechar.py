#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 13:50:02 2023

@author: rinseo
"""

"""
    find the middle char of a string
"""

usrinput = input("Enter a string: ")

# Position is the index of (length of a string floor division by 2)
# Position - 1 is the lowerbound char + Position is the upperbound char
position = len(usrinput) // 2


if len(usrinput) % 2 == 1:
    # odd number gives the middle char
    result = usrinput[position]
    
else:
    # if even number, position-1 gives the left char and position gives the right char
    result = usrinput[position-1] + usrinput[position] 
    
print("Middle character(s) in '%s' is '%s' " % (usrinput, result))
