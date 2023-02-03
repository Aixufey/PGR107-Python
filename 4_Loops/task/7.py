# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 23:13:31 2023

@author: sparrow
"""

userinput = input("Enter a word: ")

while userinput != "":
    for c in userinput:
        print(c, end = '\n')
    userinput = input("Enter a word: ")