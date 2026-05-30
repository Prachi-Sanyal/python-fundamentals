#1 Create Set
s = {1,2,3}
print(s)

#2 Add Element
s = {1,2,3}
s.add(4)
print(s)

#3 Remove Element
s = {1,2,3}
s.remove(2)
print(s)

#OR

s = {1,2,3}
s.discard(2)
print(s)

#4 Union
A = {1,2,3}
B = {3,4,5}

print(A | B)

#OR

print(A.union(B))

#5 Intersection
A = {1,2,3}
B = {3,4,5}

print(A & B)

#OR

print(A.intersection(B))

#6 Difference
A = {1,2,3}
B = {3,4,5}

print(A - B)

#7 Symmetric Difference
A = {1,2,3}
B = {3,4,5}

print(A ^ B)

#8 Remove Duplicates Using Set
numbers = [1,2,2,3,4,4]

unique = list(set(numbers))
print(unique)

#9 Check Membership
s = {1,2,3}

print(2 in s)
print(5 in s)

#10 Set Length
s = {1,2,3,4}
print(len(s))

#11 Clear Set
s = {1,2,3}
s.clear()

print(s)

#12 Frozen Set
s = frozenset([1,2,3])

print(s)