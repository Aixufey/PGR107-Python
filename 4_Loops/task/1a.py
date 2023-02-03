# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 22:13:16 2023

@author: sparrow
"""

i = 0
j = 10
n = 0

while i < j :
    i = i + 1 
    j = j - 1
    n = n + 1
    #print(f" {i} {j} {n}")

    # print('i:{0:4d}     j:{1:4d}    n:{2:4d}'.format(i, j, n))

    print('i =>{:>2}   j =>{:>2}  n =>{:>2}'.format(i,j,n))

    
# coord = (6, 10)
# print('X: {0[0]}, Y: {0[1]}'.format(coord), end=' ')