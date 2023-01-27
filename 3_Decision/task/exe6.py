# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 21:02:06 2023

@author: sparrow
"""

"""
    6
"""
import re


def regexfn():
    val = input("Enter value: ")
    match = None
    # ^start with a set of char inside [a-zA-Z] +one or more occurrences ends with$
    # re.ASCII flag parameter is optional
    
    if re.search("^[a-zA-Z]+$", val, re.ASCII):
        match = "✅ Contains only letters."
        
    if re.search("^[A-Z]+$", val, re.ASCII):
        match = "✅ Contains only uppercase letters."
    elif re.search("^[a-z]+$", val, re.ASCII):
        match = "✅ Contains only lowercase letters."
    elif re.search("^[0-9]+$", val, re.ASCII):
        match = "✅ Contains only digits."
    elif re.search("^[a-zA-Z0-9]+$", val, re.ASCII):
        match = "✅ Contains only letters and digits."
    elif re.search("^[A-Z]", val, re.ASCII):
        match = "✅ Starts with an uppercase letter."
    elif re.search("[.*\.$]", val, re.ASCII):
        match = "✅ Ends with a period."
    else:
        match = "Input does not match any conditions."
    return match

        
result = regexfn()
print("%-5s" % "Input = ", result)
