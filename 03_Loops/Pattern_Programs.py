#1 Star Pattern
for i in range(1, 5):
    print("*" * i)

#2 Reverse Star Pattern
for i in range(4, 0, -1):
    print("*" * i)

#3 Pyramid Pattern
rows = 4

for i in range(rows):

    print(" "*(rows-i-1) + "*"*(2*i+1))

#4 Inverted Pyramid
rows = 4

for i in range(rows, 0, -1):

    print(" "*(rows-i) + "*"*(2*i-1))

#5 Diamond Pattern
rows = 4

for i in range(rows):
    print(" "*(rows-i-1) + "*"*(2*i+1))

for i in range(rows-2, -1, -1):
    print(" "*(rows-i-1) + "*"*(2*i+1))

#6 Hollow Square
size = 5

for i in range(size):

    for j in range(size):

        if i == 0 or i == size-1 or j == 0 or j == size-1:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()

#7 Hollow Pyramid
rows = 5

for i in range(rows):

    for j in range(2*rows-1):

        if j == rows-i-1 or j == rows+i-1 or i == rows-1:
            print("*", end="")

        else:
            print(" ", end="")

    print()