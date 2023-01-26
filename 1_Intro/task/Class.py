# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 01:16:33 2023

@author: sparrow
"""

# Class without fields must have keyword pass

class Menu:
    pass

    # Class instance method
    def instanceMethod(this):
        print("I'm being invoked from an instance\n")

    # Class method
    def displayMenu():
        # Using list constructor here with keyword list(())
        myList = list(("1 - Coffee", "2 - Energy Drinks", "3 - Beer", "4 - Exit"))
        for l in myList:
            print(l)
            
    """
        Calling class method without `this` the method belongs to the class and not instance
        If using this.displayMenu() the method belongs to an instance
        this means we have to instantiate Menu and call runProgram from this instance
    """
    def runProgram():
        Menu.displayMenu()
        
        while True:
            # Guard Clause Concept 
            choice = input("Enter choice: ")
            if int(choice) == 4: 
                print("Thanks for shopping!")
                return
            
            if int(choice) == 1:
                print("TBA")
            elif int(choice) == 5:
                import os
                # absolutePath = os.path.dirname(os.path.abspath(__file__))
                # print(absolutePath)
                
                workingDir = os.getcwd()
                print(workingDir)
                item = "\myTxt.txt"
                f = open(workingDir + item, "r")
                print(f.read())
                #f = open("G:\Other computers\My MacBook Air\Kristiania\PGR107 Python\myTxt.txt", "r")
                #print(f.read())
                
            else:
                Menu.displayMenu()
    
    
        

myMenu = Menu()
myMenu.instanceMethod()
Menu.runProgram()

