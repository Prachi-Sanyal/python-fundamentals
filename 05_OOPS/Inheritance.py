#1 Single Inheritance
# Person -> Student

class Person:

    def display_person(self):
        print("Person Class")

class Student(Person):

    def display_student(self):
        print("Student Class")

s = Student()

s.display_person()
s.display_student()

#2 Multilevel Inheritance -------------------------
# Animal -> Dog -> Puppy

class Animal:

    def eat(self):
        print("Animal Eats")

class Dog(Animal):

    def bark(self):
        print("Dog Barks")

class Puppy(Dog):

    def weep(self):
        print("Puppy Weeps")

p = Puppy()

p.eat()
p.bark()
p.weep()

#3 Multiple Inheritance---------------------------
# Father + Mother -> Child

class Father:

    def father_property(self):
        print("Father Property")

class Mother:

    def mother_property(self):
        print("Mother Property")

class Child(Father,Mother):

    def child_property(self):
        print("Child Property")

c = Child()

c.father_property()
c.mother_property()
c.child_property()

#4 heirarchial inheritance
# Shape -> Circle

class Shape:

    def show(self):
        print("Shape")

class Circle(Shape):

    def draw_circle(self):
        print("Circle")

c = Circle()

c.show()
c.draw_circle()

# Shape -> Rectangle

class Rectangle(Shape):

    def draw_rectangle(self):
        print("Rectangle")

r = Rectangle()

r.show()
r.draw_rectangle()