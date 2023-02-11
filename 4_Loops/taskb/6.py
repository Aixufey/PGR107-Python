"""
    6. Print letter F shape

            col
          1 2 3 4 5
    row 1 * * * * *
        2 *
        3 * * * * *
        4 *
        5 *

    1. Outer forloop determines Height of F == rows
    2. Inner loop determines for each row, at column 1 (Yes, slim F)
        if the current row is 1 or 3 print all X (row 1,2,3,4,5)
        else print column 1 and rest empty string

        Outer loop:
        In range 1 to 5 + 1 means inclusive 5 and print col 1

           col 1
             1
    row 1    *
    row 2    *
    row 3    *
    row 4    *
    row 5    *

        Inner loop:
            col 1
             1 2 3 4 5
    row 1    * * * * *
    row 2
    row 3    * * * * *
    ...
    ..
"""

ROWS = 5

for row in range(1, ROWS + 1):
    for col in range(1, ROWS + 1):
        if col == 1 or (row == 1 or row == 3):
            print("X", end=' ')
        else:
            print(" ", end=' ')
    print()
