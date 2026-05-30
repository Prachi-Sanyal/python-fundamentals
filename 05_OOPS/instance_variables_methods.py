#1 Student Details Storage

class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Student("Prachi",22)

print(s1.name)
print(s1.age)

#2 Display Details Method

class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name,self.age)

s1 = Student("Prachi",22)

s1.display()

#3 Update Details Method

class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def update(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name,self.age)

s1 = Student("Prachi",22)

s1.display()

s1.update("Prachi Sanyal",23)

s1.display()