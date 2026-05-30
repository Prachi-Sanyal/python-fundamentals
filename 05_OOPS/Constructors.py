#1 Default Constructor

class Student:

    def __init__(self):
        print("Default Constructor Called")

s1 = Student()

#2 Parameterized Constructor

class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Student("Prachi",22)

print(s1.name)
print(s1.age)

#3 Another Example

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

emp = Employee("Rahul",50000)

print(emp.name)
print(emp.salary)