

"""
   trace table
   i in range 3 = 0 1 2
   j in range 5 = 0 1 2 3 4
"""
for i in range(3): # row
    for j in range(5): # column
        if j % 2 == 1:
            print('*', end=" ")
        else:
            print("-", end=" ")
    print()
print()

#####TABLE#####
ROWMAX = 10
COLMAX = 4

for i in range(1, COLMAX + 1):
    print("%10d" % i, end="")
print()
for i in range(1, COLMAX + 1):
    print("%10s" % "x ", end="")
print()
print("\t","-" * 40)

for x in range(1, ROWMAX + 1):
    for n in range(1, COLMAX + 1):
        print("%10d" % x**n, end="") # col prints x^n for current line
    print()
print("\t", "-" * 40)

# first row x = 1
#    column will print 4 times
#    x ^ n = 1 ^ 1, 1 ^ 2, 1 ^ 3, 1 ^ 4



