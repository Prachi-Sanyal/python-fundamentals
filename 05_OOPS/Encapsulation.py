#1 Public Variable

class Student:

    def __init__(self):
        self.name = "Prachi"

s = Student()

print(s.name)

#2 Protected Variable

class Student:

    def __init__(self):
        self._name = "Prachi"

s = Student()

print(s._name)

#3 Private Variable

class Student:

    def __init__(self):
        self.__name = "Prachi"

    def display(self):
        print(self.__name)

s = Student()

s.display()

#OR

print(s._Student__name)