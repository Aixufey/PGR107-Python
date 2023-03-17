"""
    The Set are stored in unsorted order
"""
my_set = {"red bull", "monster", "nocco", "coca cola", "solo"}

for i in my_set:
    print(i)
print("=" * 20)


"""
    How to sort a Set using function 'sorted'
    It will return as a List
"""

sorted_set_as_list = sorted(my_set)

for i in sorted_set_as_list:
    print(i)
print("=" * 20)


"""
    Adding (unordered) in Set
"""
my_set.add("Tea")
my_set.add("Beer")


sorted_set_as_list = sorted(my_set)
for i in sorted_set_as_list:
    print(i)


"""
    Checking for subset in a Set equality
    In mathematics a set are equals if elements are equal, no order.
"""

canadian = {"Red", "White"}
british = {"Red", "Blue", "White"}
italian = {"Red", "White", "Green"}
french = {"Red", "White", "Blue"}

print(f"canadian flag color is a subset of british: %s" %canadian.issubset(british))
print(french.issubset(british))


"""
    Union, unify uniques in both set and remove duplicates.
    Return a new set including the result
"""
print("%s is the unified." % british.union(italian))

"""
    Intersect, finding the uniques between two set
    Return only the uniques
"""
print("%s are the unique." % british.intersection(italian))

"""
    Difference, find the element not existing between two set
"""
print("%s does not exist in french flag" % italian.difference(french))

