# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 21:26:35 2023

@author: sparrow
"""

userinput = input("Write something.. ")

while userinput != "":
    a = userinput[0:1].upper();
    b = userinput[::2]
    c = userinput
    for i in "aeiouAEIOU":
        c = c.replace(i, "_")
    d = 0
    for i in userinput:
        if i.isnumeric():
            d += 1
    e = c
    for i,vowel in enumerate(userinput):
        if vowel in 'aeiouAEIOU':
            e = e.replace("_", str(i), 1)
    
    break
     
print(f"a: {a}\nb: {b}\nc: {c}\nd: {d}\ne: {e}".format(a,b,c,d,e))