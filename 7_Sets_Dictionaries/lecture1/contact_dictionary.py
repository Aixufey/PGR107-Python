contacts = {
    "Fred": 12312312,
    "Mary": 123125,
    "Sally": 5531421
}

print(len(contacts))

"""
    Python 3.7 dictionaries are sorted
    accessing keys to get values
"""
# get method accept two parameters, first being key and second is default return value
print(contacts.get("Freddy", "Not found"))

"""
    Modifying dictionary - updating values, if not exist add it as new k,v pairs
"""

contacts["Fred"] = 0
print(contacts)

contacts.update({"Fred": 0})
print(contacts)

"""
    Iterating through dictionaries amongst keys or values
"""
for item in sorted(contacts):
    print(contacts[item])

for item in contacts.values():
    print(item)

for item in contacts.keys():
    print(item)

for k, v in contacts.items():  # accessing k,v at the same time
    print(f" {k} is key and {v} is the value")
