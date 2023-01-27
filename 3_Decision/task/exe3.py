#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:53:19 2023

@author: rinseo
"""

"""
    3
"""
import timeit

def markMyGrade():
    usrinput = int(input("Enter your total score: "))
    mark = ''
    
    start = timeit.default_timer()
    
    if 0 < usrinput > 100:
        print("Score must between 0 and 100.")
        return
    elif usrinput >= 90:
        mark = 'A'
    elif usrinput >= 80:
        mark = 'B'
    elif usrinput >= 70:
        mark = 'C'
    elif usrinput >= 60:
        mark = 'D'
    else:
        mark = 'F'
        
    print("You scored mark " + mark)
    stop = timeit.default_timer()
    print("Time complexity: %.4s" % (stop - start), "s") 
    
    return mark

markMyGrade()


def markMyGradeEnhanced():
    usrinput = int(input("Enter your total score: "))
    grades = [("A", 90, 100), ("B", 80, 89), ("C", 70, 79), ("D", 60, 69), ("F", 0, 59)]
    start = timeit.default_timer()
    
    if usrinput < 0 or usrinput > 100:
        print("Enter value between 0 and 100.")
    else:
        for grade in grades:
            # is equivalent to grade[1] <= usrinput and usrinput <= grade[2]
            if grade[1] <= usrinput <= grade[2]:
                
                stop = timeit.default_timer()
                print("You scored mark ", grade[0])
                print("Time complexity: %.4s" % (stop - start), "s")  
                
markMyGradeEnhanced()

