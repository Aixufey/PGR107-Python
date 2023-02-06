# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:43:54 2023

@author: sparrow
"""

i = 10
j = 0
n = 0

while i > 0:
    i = i - 1
    j = j + 1
    n = n + i - j
    print('i: {:>2}  j: {:>2}  n: {:>2}'.format(i,j,n))
    
    
"""
    loop1:
        i = 10 - 1
        j = 0 + 1
        n = 0 + 9 - 1
    loop2:
        i = 9 - 1
        j = 1 + 1
        n = 8 + 8 - 2
    loop3:
        i = 8 - 1
        j = 2 + 1
        n = 14 + 7 - 3
    loop4:
        i = 7 - 1
        j = 3 + 1
        n = 18 + 6 - 4
    loop5:
        i = 6 - 1
        j = 4 + 1
        n = 20 + 5 - 5
    loop6:
        i = 5 - 1
        j = 5 + 1
        n = 20 + 4 - 6
    loop7:
        i = 4 - 1
        j = 6 + 1
        n = 18 + 3 - 7
    loop8:
        i = 3 - 1
        j = 7 + 1
        n = 14 + 2 - 8
    loop9:
        i = 2 - 1
        j = 8 + 1
        n = 8 + 1 - 9
    loop10:
        i = 1 - 1
        j = 9 + 1
        n = 0 + 0 - 10
"""