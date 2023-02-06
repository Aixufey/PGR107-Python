# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 20:52:53 2023

@author: sparrow
"""
import numpy

FNAME = input("Enter first name: ")
LNAME = input("Enter last name: ")

LIST = []
score = int(input("Enter scores: "))

while score != -1:
    LIST.append(score)
    score = int(input("Enter scores: "))


average = numpy.mean(LIST)

print(FNAME)
print(LNAME)

for n in LIST:
    print("{:>29}".format(n))
    
print("Your average score is => {:>6} ".format(average)) 
