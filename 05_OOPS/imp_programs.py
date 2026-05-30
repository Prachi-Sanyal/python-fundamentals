# ==================================================
# 1 BANK ACCOUNT OOPS PROJECT
# ==================================================

class BankAccount:

    bank_name = "State Bank"

    def __init__(self,account_holder,balance=0):

        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):

        self.balance += amount

        print(f"Deposited ₹{amount}")

    def withdraw(self,amount):

        if amount <= self.balance:

            self.balance -= amount

            print(f"Withdrawn ₹{amount}")

        else:

            print("Insufficient Balance")

    def check_balance(self):

        print(f"Current Balance = ₹{self.balance}")

    def display_account(self):

        print("Bank Name:",self.bank_name)
        print("Account Holder:",self.account_holder)
        print("Balance:",self.balance)

# Create Accounts

account1 = BankAccount("Prachi",10000)

account1.display_account()

# Deposit

account1.deposit(5000)

# Withdraw

account1.withdraw(3000)

# Check Balance

account1.check_balance()

print()

# Second Account

account2 = BankAccount("Rahul",2000)

account2.display_account()

account2.withdraw(2500)

account2.deposit(1000)

account2.check_balance()


# ==================================================
# 2 BANK ACCOUNT USING INHERITANCE
# ==================================================

class Account:

    def __init__(self,name,balance):

        self.name = name
        self.balance = balance

    def display(self):

        print(self.name,self.balance)

class SavingsAccount(Account):

    def add_interest(self):

        self.balance += self.balance * 0.05

s = SavingsAccount("Prachi",10000)

s.display()

s.add_interest()

s.display()


# ==================================================
# 3 LIBRARY MANAGEMENT OOPS PROJECT
# ==================================================

class Library:

    def __init__(self):

        self.books = []

    def add_book(self,book):

        self.books.append(book)

        print(f"{book} Added")

    def remove_book(self,book):

        if book in self.books:

            self.books.remove(book)

            print(f"{book} Removed")

        else:

            print("Book Not Found")

    def search_book(self,book):

        if book in self.books:

            print("Book Available")

        else:

            print("Book Not Available")

    def display_books(self):

        print("Available Books:")

        for book in self.books:

            print(book)

library = Library()

library.add_book("Python Programming")

library.add_book("Data Structures")

library.add_book("Machine Learning")

print()

library.display_books()

print()

library.search_book("Python Programming")

library.search_book("Java")

print()

library.remove_book("Data Structures")

print()

library.display_books()


# ==================================================
# 4 LIBRARY MANAGEMENT USING OBJECTS
# ==================================================

class Book:

    def __init__(self,title,author):

        self.title = title
        self.author = author

    def display(self):

        print(self.title,"-",self.author)

book1 = Book("Python","Guido")

book2 = Book("AI Basics","Andrew")

book1.display()

book2.display()


# ==================================================
# 5 EMPLOYEE MANAGEMENT SYSTEM
# ==================================================

class Employee:

    company = "ABC Pvt Ltd"

    def __init__(self,emp_id,name,salary):

        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):

        print(self.emp_id,self.name,self.salary)

    def increment_salary(self,amount):

        self.salary += amount

employees = [

    Employee(101,"Prachi",50000),
    Employee(102,"Rahul",45000),
    Employee(103,"Amit",60000)

]

for emp in employees:

    emp.display()

print()

employees[0].increment_salary(5000)

employees[0].display()


# ==================================================
# 6 STUDENT MANAGEMENT SYSTEM
# ==================================================

class Student:

    def __init__(self,roll,name,marks):

        self.roll = roll
        self.name = name
        self.marks = marks

    def display(self):

        print(self.roll,self.name,self.marks)

students = [

    Student(1,"Prachi",90),
    Student(2,"Rahul",85),
    Student(3,"Neha",95)

]

for student in students:

    student.display()


# ==================================================
# 7 POLYMORPHISM PROJECT
# ==================================================

class Shape:

    def area(self):

        pass

class Rectangle(Shape):

    def __init__(self,length,width):

        self.length = length
        self.width = width

    def area(self):

        return self.length * self.width

class Circle(Shape):

    def __init__(self,radius):

        self.radius = radius

    def area(self):

        return 3.14 * self.radius * self.radius

shapes = [

    Rectangle(10,5),
    Circle(7)

]

for shape in shapes:

    print(shape.area())


# ==================================================
# 8 ENCAPSULATION PROJECT
# ==================================================

class Bank:

    def __init__(self):

        self.__balance = 10000

    def deposit(self,amount):

        self.__balance += amount

    def withdraw(self,amount):

        if amount <= self.__balance:

            self.__balance -= amount

    def get_balance(self):

        return self.__balance

b = Bank()

print(b.get_balance())

b.deposit(5000)

print(b.get_balance())

b.withdraw(2000)

print(b.get_balance())


# ==================================================
# 9 OPERATOR OVERLOADING PROJECT
# ==================================================

class Distance:

    def __init__(self,meter):

        self.meter = meter

    def __add__(self,other):

        return Distance(self.meter + other.meter)

    def __str__(self):

        return f"{self.meter} meters"

d1 = Distance(100)

d2 = Distance(200)

d3 = d1 + d2

print(d3)


# ==================================================
# 10 MINI ATM PROJECT
# ==================================================

class ATM:

    def __init__(self,balance):

        self.balance = balance

    def deposit(self,amount):

        self.balance += amount

    def withdraw(self,amount):

        if amount <= self.balance:

            self.balance -= amount

        else:

            print("Insufficient Balance")

    def check_balance(self):

        print("Balance =",self.balance)

atm = ATM(10000)

atm.check_balance()

atm.deposit(2000)

atm.check_balance()

atm.withdraw(5000)

atm.check_balance()