#1 Right Triangle
for i in range(1, 6):
    print("*" * i)

print()


#2 Left Triangle
rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)

print()

#3 Hollow Rectangle
rows = 5
cols = 8

for i in range(rows):

    for j in range(cols):

        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()

print()

#4 Pascal Triangle
rows = 5

for i in range(rows):

    num = 1

    print(" " * (rows - i), end="")

    for j in range(i + 1):

        print(num, end=" ")

        num = num * (i - j) // (j + 1)

    print()

print()

#5 Butterfly Pattern
rows = 5

# Upper Half
for i in range(1, rows + 1):

    print("*" * i +
          " " * (2 * (rows - i)) +
          "*" * i)

# Lower Half
for i in range(rows - 1, 0, -1):

    print("*" * i +
          " " * (2 * (rows - i)) +
          "*" * i)
    
print()

#6 X Pattern
size = 5

for i in range(size):

    for j in range(size):

        if i == j or i + j == size - 1:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()

print()

#7 Number Pyramid
rows = 5

for i in range(1, rows + 1):

    print(" " * (rows - i), end="")

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

print()

#8 Floyd's Triangle
rows = 5

num = 1

for i in range(1, rows + 1):

    for j in range(i):

        print(num, end=" ")
        num += 1

    print()

print()

#9 Binary Triangle
rows = 5

for i in range(1, rows + 1):

    for j in range(1, i + 1):

        print((i + j) % 2, end=" ")

    print()

print()

#10 Hourglass Pattern
rows = 5

# Upper Part
for i in range(rows, 0, -1):

    print(" " * (rows - i) + "* " * i)

# Lower Part
for i in range(2, rows + 1):

    print(" " * (rows - i) + "* " * i)