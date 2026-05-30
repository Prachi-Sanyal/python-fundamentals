#1 Login System
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

#2 ATM menu Simulation
balance = 10000

pin = input("Enter PIN: ")

if pin == "1234":

    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = float(input("Enter amount: "))

        if amount <= balance:
            balance -= amount
            print("Remaining Balance =", balance)
        else:
            print("Insufficient Balance")

    elif choice == 3:
        amount = float(input("Enter amount: "))
        balance += amount
        print("New Balance =", balance)

    else:
        print("Invalid Choice")

else:
    print("Invalid PIN")

#3 Menu Driven Calculator
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result =", a + b)

elif choice == 2:
    print("Result =", a - b)

elif choice == 3:
    print("Result =", a * b)

elif choice == 4:
    if b != 0:
        print("Result =", a / b)
    else:
        print("Division by zero not allowed")

else:
    print("Invalid Choice")