#1 List creation
numbers = [10, 20, 30, 40]
print(numbers)

#2 Add element
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

#OR

numbers = [10, 20]
numbers.extend([30, 40])
print(numbers)

#3 Remove element
numbers = [10, 20, 30]
numbers.remove(20)
print(numbers)

#OR

numbers = [10, 20, 30]
numbers.pop()
print(numbers)

#OR

numbers = [10, 20, 30]

del numbers[1]

print(numbers)

#4 Insert element
numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)

#5 Sort List
numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)

# descending
numbers.sort(reverse=True)
print(numbers)

#6 Reverse List
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)

#OR 
print(numbers[::-1])

#7 Copy List 
list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)

#OR 
list2 = list1[:]

#8 Merge two lists
list1 = [1, 2]
list2 = [3, 4]
merged = list1 + list2
print(merged)

#9 Find largest Element
numbers = [10, 5, 40, 20]
print(max(numbers))

#OR
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)

#10 Find smallest Element
numbers = [10, 5, 40, 20]
print(min(numbers))

#11 Find duplicates
numbers = [1,2,3,2,4,5,1]

duplicates = []

for num in numbers:

    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)

#12 Remove duplicates
numbers = [1,2,3,2,4,5,1]
unique = list(set(numbers))
print(unique)

#13 List comprehension
squares = []
for i in range(1,6):
    squares.append(i*i)
print(squares)

#OR
squares = [i*i for i in range(1,6)]
print(squares)

#14 Matrix using Lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
