from abc import ABC, abstractmethod

#1 Abstract Class

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

#2 Abstract Method

class Car(Vehicle):

    def start(self):
        print("Car Starts")

c = Car()

c.start()

# Another Example

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

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