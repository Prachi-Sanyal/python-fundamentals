import csv

# ==================================================
# 1 Create CSV
# ==================================================

with open("students.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID","Name","Marks"])

    writer.writerow([1,"Prachi",90])

# ==================================================
# 2 Read CSV
# ==================================================

with open("students.csv","r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# ==================================================
# 3 Append CSV Row
# ==================================================

with open("students.csv","a",newline="") as file:

    writer = csv.writer(file)

    writer.writerow([2,"Rahul",85])

# ==================================================
# 4 Read Using DictReader
# ==================================================

with open("students.csv","r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)

# ==================================================
# 5 Update CSV
# ==================================================

rows = []

with open("students.csv","r") as file:

    reader = csv.reader(file)

    for row in reader:

        if len(row) > 0 and row[0] == "2":

            row[2] = "95"

        rows.append(row)

with open("students.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerows(rows)