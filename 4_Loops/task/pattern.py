# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:38:54 2023

@author: sparrow
"""

"""
    Pattern printing
    With the help of 2 for loop one for row and one for column
    
    
    Computer print in this direction ---> 
    
   i=1     *
   i=2     * *
   i=3     * * *
   i=4     * * * *
   i=5     * * * * *
"""
"""

nested loop = A loop within another loop (outher, inner)
                outer loop:
                    inner loop:
"""

# rows = int(input("Enter the # of rows: "))
# columns = int(input("Enter the # of columns: "))
# symbol = input("Enter the symbol to use; ")

# for x in range(rows):
#     for j in range(columns):
#         print(symbol, end=' ')
#     print()

for i in range(4):
    for j in range(4):
        print('x' ,end =' ')
    print()