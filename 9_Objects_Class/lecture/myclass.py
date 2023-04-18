class MyClass:
    x = 12
    y = 20


a = MyClass()
print(type(a))  # object of type 'MyClass'

b = MyClass()
print(type(b))

print(isinstance(a, MyClass))  # both instances a and b is an instance of 'MyClass'
print(isinstance(b, MyClass))


class EnergyDrink:
    # Private convention with double underscore __ to encapsulate
    def __init__(self, brand, price, color):
        self.__brand = brand
        self.__price = price

    # Separate method for getter
    def get_info(self):
        print(self.__brand)
        print(self.__price)


monster = EnergyDrink('Monster Ultra', '23')
monster.get_info()
