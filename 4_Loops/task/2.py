# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:27:51 2023

@author: sparrow
"""

"""
    2
"""

n = int(input("Enter a value: "))
i = 0

while (i * i) < n:
   # print comes before i increment with 1 to get the 0
   print('i: {:>2}  <  n: {:>2}'.format(i*i,n))
   i = i + 1

"""
    loop logic runs at least 1 time, or run n times so long as n is < i
        i = 0      0^2 = 0
        i = 0 + 1  1^2 = 1
        i = 1 + 1  2^2 = 4
        i = 2 + 1  3^2 = 9 
        i = 3 + 1  4^2 = 16
        i = 4 + 1  5^2 = 25
        i = 5 + 1  6^2 = 36
        i = 6 + 1  7^2 = 49
        i = 7 + 1  8^2 = 64
        i = 8 + 1  9^2 = 81
        i = 9 + 1  10^2 = 100
"""

