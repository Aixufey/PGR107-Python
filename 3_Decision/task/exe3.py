#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:53:19 2023

@author: rinseo
"""

"""
    3
"""

def markMyGrade():
    usrinput = int(input("Enter your total score: "))
    mark = ''
    
    if usrinput >= 90 and usrinput <= 100:
        mark = 'A'
    elif usrinput >= 80 and usrinput <= 89:
        mark = 'B'
    elif usrinput >= 70 and usrinput <= 79:
        mark = 'C'
    elif usrinput >= 60 and usrinput <= 69:
        mark = 'D'
    elif usrinput >= 0 and usrinput <= 60:
        mark = 'F'
    else:
        mark = 'N/A'
    print("You scored mark " + mark)
    return mark

markMyGrade()