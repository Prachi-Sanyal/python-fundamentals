'''
#1 Print Hello World
print("Hello World")

#2 User input
num=int(input("Enter a number: "))
print(num) 

#3 Input name and age
name=input("Enter your name: ")
age=int(input("Enter your age: "))
print("Name: ",name," Age: ",age)

#-------------------------------------------

#4 Swap two variables(method 1)
a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)

# Method 2 with temp variable

a = 10
b = 20
print(a, b)
temp = a
a = b
b = temp
print(a, b)

#Method 3 using Arithmetic

a = 10
b = 20
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)

#----------------------------------

#5 Multiple variable Assignment

a = b = c = 100
print(a)
print(b)
print(c)
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

#6 Check Data Type of Variable
'''
a = 10
b = 3.14
c = "Python"
d = True
e = 5+6j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#7 Type Casting 
num = 10
result = float(num)

print(result)
print(type(result))

num = "100"
result = int(num)

print(result)
print(type(result))

num = input("Enter a number: ")
num = int(num)
print(num + 10)

#8 Convert temperature C->F
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#9 Convert temperature F->c
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Celsius:", celsius)



