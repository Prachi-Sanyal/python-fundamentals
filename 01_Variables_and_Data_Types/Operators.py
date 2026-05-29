#1 Arithmetic Operators

a = 10
b = 3

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Power =", a ** b)

#2 Relational Operators

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#3 Logical Operators
a = True
b = False

print(a and b)
print(a or b)
print(not a)

#4 Assignment Operators
x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

x /= 2
print(x)

#5 Membership Operators
numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)
print(50 not in numbers)

#6 Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)

print(a == c)

'''
==  → compares values
is  → compares memory locations

'''