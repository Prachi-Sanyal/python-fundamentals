# ==================================================
# 1 Count Characters
# ==================================================

file = open("sample.txt","r")

data = file.read()

print(len(data))

file.close()

# ==================================================
# 2 Count Words
# ==================================================

file = open("sample.txt","r")

data = file.read()

print(len(data.split()))

file.close()

# ==================================================
# 3 Count Lines
# ==================================================

file = open("sample.txt","r")

print(len(file.readlines()))

file.close()

# ==================================================
# 4 Count Vowels
# ==================================================

file = open("sample.txt","r")

data = file.read().lower()

count = 0

for ch in data:

    if ch in "aeiou":
        count += 1

print(count)

file.close()

# ==================================================
# 5 Count Uppercase Letters
# ==================================================

file = open("sample.txt","r")

data = file.read()

count = 0

for ch in data:

    if ch.isupper():
        count += 1

print(count)

file.close()

# ==================================================
# 6 Search Word In File
# ==================================================

file = open("sample.txt","r")

data = file.read()

word = "python"

print(word in data.lower())

file.close()

# ==================================================
# 7 Copy Text File
# ==================================================

source = open("sample.txt","r")

data = source.read()

source.close()

target = open("copy.txt","w")

target.write(data)

target.close()