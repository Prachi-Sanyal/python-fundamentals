import math

#1 Prime number
num = int(input())

if num < 2:
    print("Not Prime")

else:
    for i in range(2, int(num**0.5)+1):

        if num % i == 0:
            print("Not Prime")
            break

    else:
        print("Prime")

#2 Prime numbers in range
start = int(input("Start: "))
end = int(input("End: "))

for num in range(start, end + 1):

    if num < 2:
        continue

    for i in range(2, int(num**0.5)+1):

        if num % i == 0:
            break

    else:
        print(num)

#3 Armstrong Number (153, 1³ + 5³ + 3³ = 153)
num = int(input())

power = len(str(num))

temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == num:
    print("Armstrong")
else:
    print("Not Armstrong")

#4 Palindrome Number
num = int(input())

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

#5 Perfect Number (6 = 1 + 2 + 3)
num = int(input())

total = 0

for i in range(1, num):

    if num % i == 0:
        total += i

if total == num:
    print("Perfect")
else:
    print("Not Perfect")

#6 Strong Number (145, 1! + 4! + 5! = 145)

num = int(input())

temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += math.factorial(digit)
    temp //= 10

if total == num:
    print("Strong")
else:
    print("Not Strong")

#7 Neon Number
'''
9

9² = 81

8 + 1 = 9
'''
num = int(input())

square = num ** 2

digit_sum = 0

while square > 0:
    digit_sum += square % 10
    square //= 10

if digit_sum == num:
    print("Neon")
else:
    print("Not Neon")

#8 Automorphic Number (25 25² = 625)
num = int(input())

square = num ** 2

if str(square).endswith(str(num)):
    print("Automorphic")
else:
    print("Not Automorphic")

#9 Duck Number (Contains zero but does not start with zero.)
num = input()

if '0' in num and num[0] != '0':
    print("Duck Number")
else:
    print("Not Duck Number")