# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:16:51 2023

@author: sparrow
"""

i = 0
j = 10
n = 0

while i != j:
    i = i + 2
    j = j - 2
    n = n + 1
    

"""
    loop1:
        i = 0 + 2      i = 2
        j = 10 - 2     j = 8
        n = 0 + 1      n = 1
    loop2:
        i = 2 + 2      i = 4
        j = 8 - 2      j = 6
        n = 1 + 1      n = 2
    loop3:
        i = 4 + 2      i = 6
        j = 6 - 2      j = 4
        n = 2 + 1      n = 3
    loop4:
        i = 6 + 2      i = 8
        j = 4 - 2      j = 2
        n = 3 + 1      n = 4
    loop5:
        i = 8 + 2      i = 10
        j = 2 - 2      j = 0
        n = 4 + 1      n = 5
    loop6:
        i = 10 + 2     i = 12
        j = 0 - 2      j = -2
        n = 5 + 1      n = 6
    ...
    ..
    .
    i is not equals to j will run forever
        
"""