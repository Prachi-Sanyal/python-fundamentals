#1 Fibonacci Series
n = int(input())

a = 0
b = 1

for i in range(n):

    print(a, end=" ")

    a, b = b, a + b

#2 Sum of Fibonacci Series
n = int(input())

a = 0
b = 1

total = 0

for i in range(n):

    total += a

    a, b = b, a + b

print(total)

#3 Generate Squares
n = int(input())

for i in range(1, n + 1):
    print(i ** 2)

#4 Generate Cubes
n = int(input())

for i in range(1, n + 1):
    print(i ** 3)

    