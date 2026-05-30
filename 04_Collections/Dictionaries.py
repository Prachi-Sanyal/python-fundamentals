#1 Create Dictionary
student = {
    "name":"Prachi",
    "age":22
}
print(student)

#2 Access Values
print(student["name"])

#OR

print(student.get("name"))

#3 Add Key Value Pair
student["city"] = "Vadodara"
print(student)

#4 Update Value
student["age"] = 23
print(student)

#5 Delete Key
del student["age"]
print(student)

#6 Loop Through Dictionary
student = {
    "name":"Prachi",
    "age":22
}

for key,value in student.items():
    print(key,value)

#7 Dictionary Keys
print(student.keys())

#8 Dictionary Values
print(student.values())

#9 Dictionary Items
print(student.items())

#10 Check Key Exists
print("name" in student)

#11 Nested Dictionary
students = {

    "student1":{
        "name":"Prachi",
        "age":22
    },

    "student2":{
        "name":"Rahul",
        "age":21
    }
}

print(students["student1"]["name"])

#12 List of Dictionaries
students = [

    {"name":"Prachi","marks":90},
    {"name":"Rahul","marks":85},
    {"name":"Amit","marks":88}
]

for student in students:
    print(student["name"], student["marks"])

#13 Merge Dictionaries
d1 = {"a":1}
d2 = {"b":2}

merged = d1 | d2

print(merged)

#14 Word Frequency Counter
text = "python is easy python is powerful"

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word,0) + 1

print(frequency)

#15 Sort Dictionary By Value
data = {
    "A":30,
    "B":10,
    "C":20
}

sorted_data = dict(sorted(data.items(), key=lambda item:item[1]))

print(sorted_data)