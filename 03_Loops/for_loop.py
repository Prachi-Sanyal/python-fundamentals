#1 Print 1 to N
n = int(input("Enter N: "))

for i in range(1, n + 1):
    print(i)

#2 Print N to 1
n = int(input("Enter N: "))

for i in range(n, 0, -1):
    print(i)

#3 Sum of First N Numbers
n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

#OR
n = int(input())

total = n * (n + 1) // 2

print(total)

#4 Multiplication Table
num = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

#5 Factorial
n = int(input("Enter number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)