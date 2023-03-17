"""
    Tuples are immutable that has less operation, no add and remove
"""
my_set = (1, 2, 3, 4, 5)
# i       0  1  2  3  4

print(len(my_set))

"""
    Normal swapping
"""
x = 10
y = 15
temp = x
x = y
y = temp

"""
    Swapping in Tuples are much more convenient
"""
(x, y) = (y, x)


def quotient_and_remainder(x, y):
    q = x // y
    r = x % y

    return q, r


(q, r) = quotient_and_remainder(4, 5)
print((q, r))
