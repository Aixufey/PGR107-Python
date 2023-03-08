# list is mutable
my_list = ['1', '2.3', 'a', 'True', 'a']

"""
string = "Python"
string[0] = "S" # error String are immutable
print(string)
"""

"""
# Referring to the same object in memory
new_list = my_list

# Getting the memory location of object in py
print(id(new_list))
print(id(my_list))


for ele in my_list:
    if 'a' in ele:
        print(ele)


# Getting index
i = new_list.index("a")
print(i)
"""

"""
# getting index of all 'a' in the list
my_other_list = ["a", "b", "c", "a", "a", "j", "g", "g"]
count = my_other_list.count("a")

if count > 0:
    n = my_other_list.index("a")
    print(n)

    for i in range(count - 1): # first 'a' is found in the latter, we exclude it
        n = my_other_list.index("a", n + 1)
        print(n)
else:
    print("'a' is not in the list")

# getting all duplicates
duplicates = []

for item in my_other_list:
    if my_other_list.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)

print(my_other_list)
print(duplicates)
"""

"""
# find position in list > 100

values = [1, 3, 254, 4, 60, 100, 88]

LIMIT = 100
pos = 0
found = False

while pos < len(values) and not found:
    if values[pos] > LIMIT:
        found = True
    else:
        pos += 1

if found:
    print("Value found at pos ", pos)
else:
    print("No element > 100")
"""

my_ints = [1, 2, 3, 4, 4, 4, 5, 4, 8, 4, 4, 3]

i = 0

while i < len(my_list):
    if my_ints[i] == 4:
        my_list.pop(i)
    else:
        # shifting index to next
        i = i + 1
