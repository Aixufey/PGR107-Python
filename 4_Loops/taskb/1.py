# a
# From index 1 till index 10: number 1 - number 9
for i in range(1, 10):
    print(i, end=' ')
print()

# b
# Increment with range step by 2
# 1 3 5 7 9
for i in range(1, 10, 2):
    print(i, end=' ')
print()

# c
# Decrement with range step by -1
# 10 9 8 7 6 5 4 3 2
for i in range(10, 1, -1):
    print(i, end=' ')
print()

# d
# 1 2 3 4 5 6 7 8 9
for i in range(10):
    print(i, end=' ')
print()

# e
# 1 - 9, if i is even print
for i in range(1, 10):
    if i % 2 == 0:
        print(i, end=' ')
