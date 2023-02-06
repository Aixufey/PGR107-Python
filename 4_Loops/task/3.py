#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 12:26:51 2023

@author: rinseo
"""

FHEADER = "\nFahrenheit    |    Celsius"
FLINER = "______________+_____________"
CHEADER = "\nCelsius       |    Fahrenheit"
CLINER = "______________+_____________"
data = []
value = []
choice = input("1 - for celsius or 2 for fahrenheit: ")

if choice != "1" and choice != "2":
    print("Invalid input.")
else:
    if choice == '1':
        userInput = input("Enter celsius: ")
        while userInput != "":
            celsius = int(userInput)
            F = int(celsius * 9/5 + 32)
            data.append(F)
            value.append(celsius)
            userInput = input("Enter celsus: ")
        print(FHEADER)
        print(FLINER)
        
        for i, val in enumerate(data):
            c = value[i]
            print(f"{val:10}\t  |\t {c:10}")
        print(FLINER)
        
    else:
        userInput = input("Enter fahrenheit: ")
        
        while userInput != "":
            fahrenheit = int(userInput)
            C = int(5/9 * (fahrenheit - 32))
            data.append(C)
            value.append(fahrenheit)
            userInput = input("Enter fahrenheit: ")
        print(CHEADER)
        print(CLINER)
        
        for i, val in enumerate(data):
            f = value[i]
            print(f"{val:10}\t  |\t {f:10}")
        print(FLINER)
