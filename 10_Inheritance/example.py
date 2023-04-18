"""
Parent class is the root
"""


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


person = Person('John', 'Wick')
person.printname()

"""
Child class can extend from parent by passing Class into constructor
"""


class Student(Person):
    def __init__(self, fname, lname, student_id=None):  # Adding new fields
        super().__init__(fname, lname)  # Call from parent
        self.student_id = student_id  # Overloading constructor

    def printname(self):
        if self.student_id:
            print(self.firstname, self.lastname, self.student_id)
        else:
            super().printname()


student = Student('John', 'Doe', 1001)
student2 = Student('Dummy', 'Student')

student.printname()
student2.printname()


"""
Multilevel inheritance Student has to be in the first argument because Student inherits from Person
"""


class Teacher(Student, Person):
    def __init__(self, fname, lname, teacher_id=None, student_id=None):
        # Person.__init__(self, fname, lname) Can be inferred
        # super().__init__(fname, lname, student_id=student_id)         # Optional 1
        Student.__init__(self, fname, lname, student_id=student_id)     # Optional 2
        self.teacher_id = teacher_id

    def printname(self):
        if self.teacher_id and self.student_id:
            print(self.firstname, self.lastname, self.teacher_id, self.student_id)


maryrock = Teacher('Mary', 'Rock', 5, 1002)
maryrock.printname()
