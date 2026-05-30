##1 list of dictionaries---------------------
#1 Create List of Dictionaries
students = [
    {"name":"Prachi","marks":90},
    {"name":"Rahul","marks":85},
    {"name":"Amit","marks":88}
]

print(students)

#2 Access Dictionary Inside List
print(students[0]["name"])

#3 Loop Through List of Dictionaries
for student in students:
    print(student["name"], student["marks"])

#4 Add New Student
students.append({
    "name":"Neha",
    "marks":92
})

print(students)

#5 Update Student Marks
students[0]["marks"] = 95

print(students)

#6 Delete Student
del students[1]

print(students)

#7 Search Student
search_name = "Amit"

for student in students:

    if student["name"] == search_name:
        print(student)

#8 Find Top Scorer
topper = students[0]

for student in students:

    if student["marks"] > topper["marks"]:
        topper = student

print(topper)

#9 Sort By Marks
students.sort(key=lambda x:x["marks"])

print(students)

#10 Sort By Name
students.sort(key=lambda x:x["name"])

print(students)

##2 Student record system ----------------------

#1 Create Student Record System
students = {}

#2 Add Student
roll = input("Enter Roll Number: ")
name = input("Enter Name: ")

students[roll] = name

print(students)

#3 Add Multiple Students
for i in range(2):

    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")

    students[roll] = name

print(students)

#4 Search Student
roll = input("Enter Roll Number To Search: ")

if roll in students:
    print(students[roll])

else:
    print("Student Not Found")

#5 Update Student
roll = input("Enter Roll Number To Update: ")

if roll in students:

    students[roll] = input("Enter New Name:")

print(students)

#6 Delete Student
roll = input("Enter Roll Number To Delete: ")

if roll in students:

    del students[roll]

print(students)

#7 Display All Students
for roll,name in students.items():

    print(roll,name)

##3 Contact book------------------------------

#1 Create Contact Book
contacts = {}

#2 Add Contact
name = input("Enter Name: ")
phone = input("Enter Phone Number: ")

contacts[name] = phone

print(contacts)

#3 Search Contact
search = input("Search Contact: ")

print(contacts.get(search,"Not Found"))

#4 Update Contact
name = input("Enter Contact Name To Update: ")

if name in contacts:

    contacts[name] = input("Enter New Number: ")

print(contacts)

#5 Delete Contact
name = input("Enter Contact Name To Delete: ")

if name in contacts:

    del contacts[name]

print(contacts)

#6 Display Contacts
for name,phone in contacts.items():

    print(name,phone)

#7 Count Contacts
print(len(contacts))

##4 Inventory System -------------------------------
#1 Create Inventory
inventory = {
    "Laptop":10,
    "Mouse":25,
    "Keyboard":15
}

print(inventory)

#2 Check Product Availability
product = input("Enter Product: ")

print(inventory.get(product,"Not Available"))

#3 Add Product
inventory["Monitor"] = 8

print(inventory)

#4 Update Stock
inventory["Laptop"] = 20

print(inventory)

#5 Reduce Stock After Sale
inventory["Mouse"] -= 1

print(inventory)

#6 Delete Product
del inventory["Keyboard"]

print(inventory)

#7 Display Inventory
for product,quantity in inventory.items():

    print(product,quantity)

#8 Total Products
print(len(inventory))

##5 Word frequency counter -----------------------------

#1 Count Word Frequency
text = input("Enter Sentence: ")

words = text.split()

frequency = {}

for word in words:

    frequency[word] = frequency.get(word,0) + 1

print(frequency)

#2 Display Frequency Line By Line
for word,count in frequency.items():

    print(word,"=",count)

#3 Most Frequent Word
max_word = max(frequency,key=frequency.get)

print(max_word)

#4 Unique Words Count
print(len(frequency))

#5 Sort By Frequency
sorted_frequency = dict(
    sorted(
        frequency.items(),
        key=lambda item:item[1],
        reverse=True
    )
)

print(sorted_frequency)

