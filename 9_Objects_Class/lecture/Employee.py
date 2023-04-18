class Employee:
    def __init__(self, name, salary, age):
        # protected doesn't prohibit modifying the attribute
        self._name = name
        self._salary = salary
        # Even private doesn't provide full encapsulation, we can still set the age
        self.__age = age

    def get_info(self):
        print(self.__age)


e1 = Employee('James', 50000, 30)
print(e1._name)

e1._name = "Jack"

print(e1._name)

e1.__age = 30
print(e1.__age)

# However, if you access without setter, it will throw AttributeError
# print(e1.__age)

# Accessing a "Private" convention in Python, this will work
print(e1._Employee__age)
