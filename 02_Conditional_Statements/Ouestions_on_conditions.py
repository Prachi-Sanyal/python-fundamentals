#1 Leap Year
year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")

#2 Checl for Voting Eligibility
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

#3 Grade Calculator
marks = float(input("Enter marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"

print("Grade =", grade)

#4 Electricity Bill Calculation
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Bill Amount =", bill)

#5 Check triangle type
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

if a == b == c:
    print("Equilateral Triangle")

elif a == b or b == c or a == c:
    print("Isosceles Triangle")

else:
    print("Scalene Triangle")

#6 Check Valid Triangle
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

#7 Check Character Vowel or consonant
ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#OR

ch = input("Enter character: ").lower()

vowels = ['a', 'e', 'i', 'o', 'u']

if ch in vowels:
    print("Vowel")
else:
    print("Consonant")

#8 Check uppercase or Lowercase
ch = input("Enter character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Not an Alphabet")

#9 Check divisibility by 5 and 11
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not Divisible")

#Check: Divisible by 5 only Divisible by 11 only Divisible by both Neither
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both")

elif num % 5 == 0:
    print("Divisible by 5 only")

elif num % 11 == 0:
    print("Divisible by 11 only")

else:
    print("Not divisible by either")