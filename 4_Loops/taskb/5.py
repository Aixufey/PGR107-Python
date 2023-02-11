
"""
    5. Print this shape

    *
    **
    ***
    ****
    *****

    Need two for loops to define structure of a shape that is n rows and n columns

"""

ROWS = 5
for row in range(1, ROWS + 1):
    for col in range(1, row + 1):
        print("* ", end="")
    print()
"""
    starting from range 1, until N of rows, not inclusive therefore we add + 1
    nested forloop: starting from range 1, until n of row, print same amount of columns as current number of row
    when nested forloop is done, go out of loop and print new line
    repeat for next row..
"""