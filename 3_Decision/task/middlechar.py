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

position = len(usrinput) // 2


if len(usrinput) % 2 == 1:
    print("odd")
    result = usrinput[position]
    
else:
    print("even")
    result = usrinput[position-1] + usrinput[position] 
    
print("Middle character(s) in '%s' is '%s' " % (usrinput, result))

# if int(len(usrinput)) % 2 == 1:
#     # odd number gives the middle char
#     result = usrinput[position]
# else:
#     # if even number, position-1 gives the left char and position gives the right char
#     result = usrinput[position-1] + usrinput[position]

# print("Middle character(s) in '%s' is '%s' " % (usrinput, result))
