# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 23:17:35 2023

@author: sparrow
"""

userinput = input("Enter a word: ")

while userinput != "":
    # slicing notation in python consist of [`start`:`stop`:`step`]
    # `start` and `stop` are optional, set to `0` and `len(the sequence)`, but here is omitted, only `step` is set to `-1`
    # the last `step` indicates the number of indices to move for each iteration.
    reverse = userinput[::-1]
    print(reverse)
    userinput = input("Enter a word: ")