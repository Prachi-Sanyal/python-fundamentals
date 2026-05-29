import math

#1 Area of Rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area =", area)

#2 Area of Circle

radius = float(input("Enter radius: "))

area = math.pi * radius ** 2

print("Area =", area)

# without math module
radius = float(input("Enter radius: "))

area = 3.14159 * radius ** 2

print("Area =", area)

#3 Simple Interest
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

si = (principal * rate * time) / 100

print("Simple Interest =", si)

#4 Compound Interest
principal = float(input("Enter principal: "))
rate = float(input("Enter annual rate (%): "))
time = float(input("Enter time in years: "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Compound Interest =", compound_interest)
print("Total Amount =", amount)

#5 Calculate BMI
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

print("BMI =", round(bmi, 2))

# another
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

print("BMI =", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

#6 Convert Days to Years, Months, Days
days = int(input("Enter total days: "))

years = days // 365
remaining_days = days % 365

months = remaining_days // 30
days_left = remaining_days % 30

print("Years =", years)
print("Months =", months)
print("Days =", days_left)

#7 Convert Seconds to HH:MM:SS
seconds = int(input("Enter seconds: "))

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")

#alternate

total_seconds = int(input("Enter seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")