# ==================================================
# 1 Read File Using With
# ==================================================

with open("sample.txt","r") as file:

    print(file.read())

# ==================================================
# 2 Write File Using With
# ==================================================

with open("sample.txt","w") as file:

    file.write("Python Programming")

# ==================================================
# 3 Append Using With
# ==================================================

with open("sample.txt","a") as file:

    file.write("\nFile Handling")

# ==================================================
# 4 Read Line By Line
# ==================================================

with open("sample.txt","r") as file:

    for line in file:

        print(line,end="")