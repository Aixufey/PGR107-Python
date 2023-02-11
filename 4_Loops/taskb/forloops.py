course = "PGR107"

# For-loop in PY loops element
for letter in course:
    print(letter, end=' ')

# While loop index
i = 0
while i < len(course):
    print(course[i], end=' ')
    i = i + 1
print()

# 1 until 10, not including 10
for i in range(1, 10):
    print(i, end=' ')
# while version
i = 1
while i < 10:
    print(i, end=' ')
    i = i + 1
print()

# Third parameter specify increment/steps
for i in range(1, 10, 2):
    print(i, end=' ')
i = 1
# While version
while i < 10:
    print(i, end=' ')
    i = i + 2
print()

# Negative
for i in range(10, 1, -1):
    print(i, end=' ')

