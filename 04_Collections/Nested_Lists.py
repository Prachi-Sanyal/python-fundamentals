#1 Matrix using Lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)

#2 Access Matrix Element
print(matrix[1][2])

#3 Matrix Addition
A = [
    [1,2],
    [3,4]
]

B = [
    [5,6],
    [7,8]
]

result = []

for i in range(len(A)):

    row = []

    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])

    result.append(row)

print(result)

#4 Matrix Transpose
matrix = [
    [1,2,3],
    [4,5,6]
]

transpose = []

for col in range(len(matrix[0])):

    row = []

    for r in range(len(matrix)):
        row.append(matrix[r][col])

    transpose.append(row)

print(transpose)

#5 Flatten Nested List
matrix = [
    [1,2],
    [3,4],
    [5,6]
]

flat = []

for row in matrix:
    for item in row:
        flat.append(item)

print(flat)

#6 Nested List Traversal
matrix = [
    [1,2,3],
    [4,5,6]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

#7 Sum of Matrix Elements
matrix = [
    [1,2,3],
    [4,5,6]
]

total = 0

for row in matrix:
    for item in row:
        total += item

print(total)

#8 Largest Element in Matrix
matrix = [
    [1,2,3],
    [4,50,6]
]

largest = matrix[0][0]

for row in matrix:
    for item in row:
        if item > largest:
            largest = item

print(largest)