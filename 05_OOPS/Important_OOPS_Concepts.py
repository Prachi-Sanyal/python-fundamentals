# ==================================================
# 1 Method Overloading
# ==================================================

# Python directly method overloading support nahi karta

class Calculator:

    def add(self,a,b,c=0):
        return a+b+c

calc = Calculator()

print(calc.add(10,20))
print(calc.add(10,20,30))

# ==================================================
# 2 Method Overriding
# ==================================================

class Parent:

    def show(self):
        print("Parent Method")

class Child(Parent):

    def show(self):
        print("Child Method")

c = Child()

c.show()

# ==================================================
# 3 Calling Parent Method Using super()
# ==================================================

class Parent:

    def show(self):
        print("Parent Method")

class Child(Parent):

    def show(self):

        super().show()

        print("Child Method")

c = Child()

c.show()

# ==================================================
# 4 Operator Overloading
# ==================================================

class Number:

    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)

# ==================================================
# 5 Constructor Chaining
# ==================================================

class Parent:

    def __init__(self):
        print("Parent Constructor")

class Child(Parent):

    def __init__(self):

        super().__init__()

        print("Child Constructor")

c = Child()

# ==================================================
# 6 Multiple Constructors
# ==================================================

# Python me multiple constructors nahi hote

class Student:

    def __init__(self,name=None,age=None):

        self.name = name
        self.age = age

s1 = Student()

s2 = Student("Prachi")

s3 = Student("Prachi",22)

print(s1.name,s1.age)
print(s2.name,s2.age)
print(s3.name,s3.age)

# ==================================================
# 7 Destructor
# ==================================================

class Student:

    def __init__(self):
        print("Constructor Called")

    def __del__(self):
        print("Destructor Called")

s = Student()

del s

# ==================================================
# 8 Garbage Collection
# ==================================================

import gc

class Test:

    pass

obj = Test()

print(gc.isenabled())

del obj

gc.collect()

print("Garbage Collection Done")

# ==================================================
# 9 Class Variable
# ==================================================

class Student:

    college = "ABC College"

    def __init__(self,name):
        self.name = name

s1 = Student("Prachi")
s2 = Student("Rahul")

print(s1.college)
print(s2.college)

# ==================================================
# 10 Instance Variable
# ==================================================

class Student:

    def __init__(self,name):
        self.name = name

s1 = Student("Prachi")
s2 = Student("Rahul")

print(s1.name)
print(s2.name)

# ==================================================
# 11 Static Method
# ==================================================

class Math:

    @staticmethod
    def add(a,b):
        return a+b

print(Math.add(10,20))

# ==================================================
# 12 Class Method
# ==================================================

class Student:

    college = "ABC College"

    @classmethod
    def change_college(cls,new_name):

        cls.college = new_name

Student.change_college("XYZ College")

print(Student.college)

# ==================================================
# 13 Instance Method
# ==================================================

class Student:

    def display(self):

        print("Instance Method")

s = Student()

s.display()

# ==================================================
# 14 isinstance()
# ==================================================

class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(isinstance(d,Dog))
print(isinstance(d,Animal))

# ==================================================
# 15 issubclass()
# ==================================================

class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog,Animal))

# ==================================================
# 16 Dynamic Attribute Creation
# ==================================================

class Student:
    pass

s = Student()

s.name = "Prachi"
s.age = 22

print(s.name)
print(s.age)

# ==================================================
# 17 Object Count
# ==================================================

class Student:

    count = 0

    def __init__(self):

        Student.count += 1

s1 = Student()
s2 = Student()
s3 = Student()

print(Student.count)

# ==================================================
# 18 Duck Typing
# ==================================================

class Duck:

    def sound(self):
        print("Quack")

class Dog:

    def sound(self):
        print("Bark")

def make_sound(obj):

    obj.sound()

make_sound(Duck())

make_sound(Dog())

# ==================================================
# 19 MRO (Method Resolution Order)
# ==================================================

class A:

    def show(self):
        print("A")

class B(A):

    pass

class C(A):

    pass

class D(B,C):

    pass

print(D.mro())

# ==================================================
# 20 __str__()
# ==================================================

class Student:

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"Student Name = {self.name}"

s = Student("Prachi")

print(s)

# ==================================================
# 21 __repr__()
# ==================================================

class Student:

    def __repr__(self):
        return "Student Object"

s = Student()

print(repr(s))

# ==================================================
# 22 Getter and Setter
# ==================================================

class Student:

    def __init__(self):

        self.__name = ""

    def set_name(self,name):

        self.__name = name

    def get_name(self):

        return self.__name

s = Student()

s.set_name("Prachi")

print(s.get_name())

# ==================================================
# 23 Property Decorator
# ==================================================

class Student:

    def __init__(self):

        self.__name = ""

    @property
    def name(self):

        return self.__name

    @name.setter
    def name(self,value):

        self.__name = value

s = Student()

s.name = "Prachi"

print(s.name)

# ==================================================
# 24 Abstract Base Class Example
# ==================================================

from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):

        print("Car Starts")

c = Car()

c.start()

# ==================================================
# 25 Runtime Polymorphism
# ==================================================

class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Dog Bark")

class Cat(Animal):

    def sound(self):
        print("Cat Meow")

animals = [Dog(),Cat()]

for animal in animals:

    animal.sound()