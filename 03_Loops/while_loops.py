#1 Print 1 to N
n = int(input())

i = 1

while i <= n:
    print(i)
    i += 1

#2 Print N to 1
n = int(input())

while n >= 1:
    print(n)
    n -= 1

#3 Sum of first N Numbers
n = int(input())

i = 1
total = 0

while i <= n:
    total += i
    i += 1

print(total)

#4 Multiplication table
num = int(input())

i = 1

while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i += 1

#5 Factorial
n = int(input())

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print(fact)
