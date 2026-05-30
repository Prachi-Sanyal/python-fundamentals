for i in range(1, 5):

    for j in range(i):
        print(chr(65+j), end="")

    print()

print()

for i in range(1, 5):
    print(chr(64+i) * i)