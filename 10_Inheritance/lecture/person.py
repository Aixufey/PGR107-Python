class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print(self):
        print(f"%s %s" % (self.fname, self.lname))


class Student(Person):
    def __init__(self, fname, lname, student_id=None):
        # Person.__init__(self, fname, lname)  Can specify Parent class or super().
        super().__init__(fname, lname)
        self.id = student_id

    def print(self):
        # Alternative 1
        Person.print(self)
        print(self.id)

        # Alternative 2
        if self.id:
            print(self.fname, self.lname, self.id)
        else:
            super().print()


p1 = Person("John", "Doe")
p1.print()

s1 = Student("Jack", "Sparrow", 101)
s1.print()
