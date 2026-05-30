#1 Create Tuple
t = (10,20,30)
print(t)

#2 Access Tuple
t = (10,20,30)
print(t[1])

#3 Tuple Slicing
t = (10,20,30,40,50)
print(t[1:4])

#4 Count Element
t = (1,2,2,2,3)
print(t.count(2))

#5 Index Element
t = (10,20,30)
print(t.index(20))

#6 Convert List to Tuple
numbers = [1,2,3]
t = tuple(numbers)
print(t)

#7 Convert Tuple to List
t = (1,2,3)
numbers = list(t)
print(numbers)

#8 Tuple Concatenation
t1 = (1,2)
t2 = (3,4)
print(t1 + t2)

#9 Tuple Repetition
t = (1,2)
print(t * 3)

#10 Tuple Unpacking
t = (10,20,30)
a,b,c = t

print(a)
print(b)
print(c)

#11 Nested Tuple
t = (
    (1,2),
    (3,4)
)

print(t[1][0])

#12 Check Element Exists
t = (10,20,30)

print(20 in t)
print(50 in t)