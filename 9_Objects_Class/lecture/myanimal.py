class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None

    # Printing method one
    def get_info(self):
        return f"{self.name} age is %s " % self.age

    # Printing method two
    def __str__(self):
        return "Animal: " + self.name + "-->" + str(self.age)

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


fido = Animal(8)
fido.set_name('Fido')
info = fido.get_info()
print(info)
print(fido)
