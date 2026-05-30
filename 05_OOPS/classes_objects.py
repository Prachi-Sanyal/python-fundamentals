#1 Student Class

class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

student1 = Student("Prachi",22)

print(student1.name)
print(student1.age)

#2 Employee Class

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

employee1 = Employee("Rahul",50000)

print(employee1.name)
print(employee1.salary)

#3 Bank Account Class

class BankAccount:

    def __init__(self,holder,balance):
        self.holder = holder
        self.balance = balance

account = BankAccount("Prachi",10000)

print(account.holder)
print(account.balance)