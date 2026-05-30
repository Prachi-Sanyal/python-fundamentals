#1 Built-in Polymorphism

print(len("Python"))

print(len([1,2,3,4]))

print(len((10,20,30)))

#2 User Defined Polymorphism

class Calculator:

    def add(self,a,b,c=0):
        return a+b+c

calc = Calculator()

print(calc.add(10,20))

print(calc.add(10,20,30))

#OR

class Shape:

    def area(self):
        print("Area")

class Circle(Shape):

    def area(self):
        print("Circle Area")

class Rectangle(Shape):

    def area(self):
        print("Rectangle Area")

c = Circle()
r = Rectangle()

c.area()
r.area()


#3 Method overriding
# Parent Class Method

class Parent:

    def show(self):
        print("Parent Method")

# Child Override

class Child(Parent):

    def show(self):
        print("Child Method")

c = Child()

c.show()

#OR

p = Parent()

p.show()