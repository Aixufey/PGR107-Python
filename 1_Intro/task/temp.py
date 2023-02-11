# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Test from Spyder")

NUMBER = 10

print("variable number = ", type(NUMBER))

print("5 + 5 = ", 5 + 5)

list = [1, 2, 3, 4, 5]
print(list[0])

print("The length of list is : ",len(list))


for x in list:
    print("number: ", x)
    
    if(x == 3):
        print("yes")
    else:
        print("no")
