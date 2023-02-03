# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:18:36 2023

@author: sparrow
"""

i = 0
j = 0
n = 0

while i < 10:
    i += 1
    n += i + j # n = n + i + j // 0 = 0 + 0 + 0
    j += 1
    print('i=> {0:2}    n=> {1:2}       j=> {2:2}'.format(i,n,j))

"""
    loop1:
        i = 0 + 1
        n = 0 + 1 + 0
        j = 0 + 1
    loop2:
        i = 1 + 1
        n = 1 + 2 + 1 
        j = 1 + 1
    loop3:
        i = 2 + 1
        n = 4 + 3 + 2
        j = 2 + 1
    loop4:
        i = 3 + 1
        n = 9 + 4 + 3
        j = 3 + 1
    loop5:
        i = 4 + 1
        n = 16 + 5 + 4
        j = 4 + 1
    loop6:
        i = 5 + 1
        n = 25 + 6 + 5
        j = 5 + 1
    loop7:
        i = 6 + 1
        n = 36 + 7 + 6
        j = 6 + 1
    loop8:
        i = 7 + 1
        n = 49 + 8 + 7
        j + 7 + 1
    loop9:
        i = 8 + 1
        n = 64 + 9 + 8
        j = 8 + 1
    loop10:
        i = 9 + 1
        n = 81 + 10 + 9
        j = 9 + 1
"""
