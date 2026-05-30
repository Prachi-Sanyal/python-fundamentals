# ==================================================
# 1 Copy One File To Another
# ==================================================

with open("source.txt","r") as source:

    data = source.read()

with open("destination.txt","w") as destination:

    destination.write(data)

# ==================================================
# 2 Count Frequency Of Characters
# ==================================================

with open("sample.txt","r") as file:

    data = file.read()

frequency = {}

for ch in data:

    frequency[ch] = frequency.get(ch,0) + 1

print(frequency)

# ==================================================
# 3 Count Frequency Of Words
# ==================================================

with open("sample.txt","r") as file:

    words = file.read().split()

frequency = {}

for word in words:

    frequency[word] = frequency.get(word,0) + 1

print(frequency)

# ==================================================
# 4 Find Longest Word
# ==================================================

with open("sample.txt","r") as file:

    words = file.read().split()

print(max(words,key=len))

# ==================================================
# 5 Remove Empty Lines
# ==================================================

with open("sample.txt","r") as file:

    lines = file.readlines()

with open("clean.txt","w") as file:

    for line in lines:

        if line.strip():

            file.write(line)

# ==================================================
# 6 Merge Two Files
# ==================================================

with open("file1.txt","r") as f1:

    data1 = f1.read()

with open("file2.txt","r") as f2:

    data2 = f2.read()

with open("merged.txt","w") as f3:

    f3.write(data1)
    f3.write("\n")
    f3.write(data2)

# ==================================================
# 7 Compare Two Files
# ==================================================

with open("file1.txt","r") as f1:

    data1 = f1.read()

with open("file2.txt","r") as f2:

    data2 = f2.read()

print(data1 == data2)

# ==================================================
# 8 Student Record CSV Project
# ==================================================

import csv

with open("students.csv","a",newline="") as file:

    writer = csv.writer(file)

    writer.writerow([101,"Prachi",90])

# ==================================================
# 9 JSON Configuration File
# ==================================================

import json

settings = {

    "theme":"dark",
    "font_size":14
}

with open("settings.json","w") as file:

    json.dump(settings,file)

# ==================================================
# 10 Exception Handling With Files
# ==================================================

try:

    with open("sample.txt","r") as file:

        print(file.read())

except FileNotFoundError:

    print("File Not Found")

# ==================================================
# 1 FILE POINTER - tell()
# ==================================================

file = open("sample.txt","r")

print(file.tell())

file.read(5)

print(file.tell())

file.close()


# ==================================================
# 2 FILE POINTER - seek()
# ==================================================

file = open("sample.txt","r")

print(file.read(5))

file.seek(0)

print(file.read(5))

file.close()


# ==================================================
# 3 tell() + seek() Together
# ==================================================

file = open("sample.txt","r")

print(file.tell())

file.read(10)

print(file.tell())

file.seek(0)

print(file.tell())

file.close()


# ==================================================
# 4 PICKLE MODULE - SAVE OBJECT
# ==================================================

import pickle

student = {
    "name":"Prachi",
    "marks":90
}

with open("student.pkl","wb") as file:

    pickle.dump(student,file)


# ==================================================
# 5 PICKLE MODULE - LOAD OBJECT
# ==================================================

with open("student.pkl","rb") as file:

    data = pickle.load(file)

print(data)


# ==================================================
# 6 PICKLE LIST
# ==================================================

numbers = [10,20,30,40,50]

with open("numbers.pkl","wb") as file:

    pickle.dump(numbers,file)

with open("numbers.pkl","rb") as file:

    data = pickle.load(file)

print(data)


# ==================================================
# 7 ZIP FILE CREATE
# ==================================================

import zipfile

with zipfile.ZipFile("files.zip","w") as zip_file:

    zip_file.write("sample.txt")


# ==================================================
# 8 ZIP FILE EXTRACT
# ==================================================

with zipfile.ZipFile("files.zip","r") as zip_file:

    zip_file.extractall("ExtractedFiles")


# ==================================================
# 9 ZIP MULTIPLE FILES
# ==================================================

with zipfile.ZipFile("backup.zip","w") as zip_file:

    zip_file.write("sample.txt")
    zip_file.write("copy.txt")


# ==================================================
# 10 LOGGING MODULE BASIC
# ==================================================

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Program Started")


# ==================================================
# 11 LOGGING LEVELS
# ==================================================

logging.debug("Debug Message")

logging.info("Info Message")

logging.warning("Warning Message")

logging.error("Error Message")

logging.critical("Critical Message")


# ==================================================
# 12 LOGGING WITH FORMAT
# ==================================================

logging.basicConfig(

    filename="app2.log",

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)

logging.info("Application Running")


# ==================================================
# 13 CONFIG FILE WRITE
# ==================================================

import configparser

config = configparser.ConfigParser()

config["DATABASE"] = {

    "host":"localhost",
    "user":"root",
    "password":"1234"
}

with open("config.ini","w") as file:

    config.write(file)


# ==================================================
# 14 CONFIG FILE READ
# ==================================================

config = configparser.ConfigParser()

config.read("config.ini")

print(config["DATABASE"]["host"])

print(config["DATABASE"]["user"])


# ==================================================
# 15 TEMPORARY FILE
# ==================================================

import tempfile

temp = tempfile.TemporaryFile()

temp.write(b"Hello Python")

temp.seek(0)

print(temp.read())

temp.close()


# ==================================================
# 16 TEMPORARY FILE WITH NAME
# ==================================================

with tempfile.NamedTemporaryFile() as temp:

    print(temp.name)


# ==================================================
# 17 EXCEPTION HANDLING WITH FILES
# ==================================================

try:

    file = open("abc.txt","r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File Not Found")


# ==================================================
# 18 MULTIPLE EXCEPTIONS
# ==================================================

try:

    file = open("sample.txt","r")

    print(file.read())

except FileNotFoundError:

    print("File Missing")

except PermissionError:

    print("Permission Denied")


# ==================================================
# 19 FINALLY BLOCK
# ==================================================

try:

    file = open("sample.txt","r")

    print(file.read())

except FileNotFoundError:

    print("Not Found")

finally:

    print("Execution Finished")


# ==================================================
# 20 DIRECTORY TRAVERSAL
# ==================================================

import os

for item in os.listdir():

    print(item)


# ==================================================
# 21 WALK THROUGH DIRECTORY
# ==================================================

for root,dirs,files in os.walk("."):

    print("Folder:",root)

    print("Directories:",dirs)

    print("Files:",files)


# ==================================================
# 22 FIND ALL PY FILES
# ==================================================

for root,dirs,files in os.walk("."):

    for file in files:

        if file.endswith(".py"):

            print(file)


# ==================================================
# 23 CSV STUDENT MANAGEMENT PROJECT
# ==================================================

import csv

with open("students.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID","Name","Marks"])

    writer.writerow([1,"Prachi",90])

    writer.writerow([2,"Rahul",85])


# Read Students

with open("students.csv","r") as file:

    reader = csv.reader(file)

    for row in reader:

        print(row)


# ==================================================
# 24 APPEND STUDENT CSV
# ==================================================

with open("students.csv","a",newline="") as file:

    writer = csv.writer(file)

    writer.writerow([3,"Amit",88])


# ==================================================
# 25 SEARCH STUDENT CSV
# ==================================================

with open("students.csv","r") as file:

    reader = csv.reader(file)

    for row in reader:

        if len(row) > 1 and row[1] == "Prachi":

            print(row)


# ==================================================
# 26 JSON EMPLOYEE MANAGEMENT PROJECT
# ==================================================

import json

employees = [

    {
        "id":101,
        "name":"Prachi",
        "salary":50000
    },

    {
        "id":102,
        "name":"Rahul",
        "salary":45000
    }
]

with open("employees.json","w") as file:

    json.dump(employees,file,indent=4)


# ==================================================
# 27 READ EMPLOYEES JSON
# ==================================================

with open("employees.json","r") as file:

    data = json.load(file)

print(data)


# ==================================================
# 28 ADD EMPLOYEE JSON
# ==================================================

with open("employees.json","r") as file:

    employees = json.load(file)

employees.append({

    "id":103,
    "name":"Amit",
    "salary":60000
})

with open("employees.json","w") as file:

    json.dump(employees,file,indent=4)


# ==================================================
# 29 SEARCH EMPLOYEE JSON
# ==================================================

with open("employees.json","r") as file:

    employees = json.load(file)

for employee in employees:

    if employee["name"] == "Prachi":

        print(employee)


# ==================================================
# 30 FILE UPLOAD SIMULATION
# ==================================================

source_file = "sample.txt"

destination_file = "uploaded_sample.txt"

with open(source_file,"rb") as source:

    data = source.read()

with open(destination_file,"wb") as destination:

    destination.write(data)

print("File Uploaded")


# ==================================================
# 31 FILE DOWNLOAD SIMULATION
# ==================================================

source_file = "uploaded_sample.txt"

destination_file = "downloaded_sample.txt"

with open(source_file,"rb") as source:

    data = source.read()

with open(destination_file,"wb") as destination:

    destination.write(data)

print("File Downloaded")


# ==================================================
# 32 IMAGE UPLOAD SIMULATION
# ==================================================

with open("image.jpg","rb") as source:

    image_data = source.read()

with open("uploaded_image.jpg","wb") as destination:

    destination.write(image_data)

print("Image Uploaded")


# ==================================================
# 33 IMAGE DOWNLOAD SIMULATION
# ==================================================

with open("uploaded_image.jpg","rb") as source:

    image_data = source.read()

with open("downloaded_image.jpg","wb") as destination:

    destination.write(image_data)

print("Image Downloaded")


# ==================================================
# 34 BACKUP ENTIRE FILE
# ==================================================

with open("sample.txt","r") as source:

    data = source.read()

with open("backup_sample.txt","w") as backup:

    backup.write(data)

print("Backup Created")


# ==================================================
# 35 FILE SIZE
# ==================================================

import os

print(os.path.getsize("sample.txt"),"Bytes")


# ==================================================
# 36 LAST MODIFIED TIME
# ==================================================

import os
import time

timestamp = os.path.getmtime("sample.txt")

print(time.ctime(timestamp))