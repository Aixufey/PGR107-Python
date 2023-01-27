# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 00:00:12 2023

@author: sparrow
"""
import sparrowDb as db



        
db.Connect('aaa.db').createConn()




class Sparrow:
    pass
    

    def displayMenu(this):
        myASCII = """
        +--------------------------------------------------------------------+
        |           .-.                                                      |
        |     .--.-'                                                         |
        |    (  (_)       .-.    .-.      ).--.    ).--.   .-._.  `)    (    |
        |     `-.         /  )  (  |     /        /       (   )   /  .   )   |
        |   _    )       /`-'    `-'-'  /        /         `-'   (_.' `-'    |
        |  (_.--'       /                                                    |
        |                                                                    |
        +--------------------------------------------------------------------+
        """
        print(myASCII)
        menuList = ["1 - test", "2 - test", "3 - test"]
        for m in menuList:

            print("%-5s " % " ", m)

            
       
            
    def runProgram(this):
        
        Sparrow.displayMenu(this)
        while True:
            usrinput = input("        Enter choice: ")
            
            if usrinput == '1':

                print("%-6s " % " ", usrinput)

                db.Connect('test.db').createConn()
                
            elif usrinput == '2':
                print('2')
            elif usrinput == '3':
                print('3')
            elif usrinput == '4':
                break
            else:
                print('N/A')
                Sparrow().displayMenu()
            
            
            
    


Sparrow().runProgram()

