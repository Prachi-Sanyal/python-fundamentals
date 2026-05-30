# ==================================================
# r Mode
# ==================================================

file = open("sample.txt","r")

print(file.read())

file.close()

# ==================================================
# w Mode
# ==================================================

file = open("sample.txt","w")

file.write("New Data")

file.close()

# ==================================================
# a Mode
# ==================================================

file = open("sample.txt","a")

file.write("\nAppend Data")

file.close()

# ==================================================
# r+ Mode
# ==================================================

file = open("sample.txt","r+")

print(file.read())

file.write("\nExtra Data")

file.close()

# ==================================================
# w+ Mode
# ==================================================

file = open("sample.txt","w+")

file.write("Python")

file.seek(0)

print(file.read())

file.close()

# ==================================================
# a+ Mode
# ==================================================

file = open("sample.txt","a+")

file.write("\nNew Line")

file.seek(0)

print(file.read())

file.close()