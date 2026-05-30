# ==================================================
# 1 Read Binary File
# ==================================================

file = open("image.jpg","rb")

data = file.read()

print(type(data))

file.close()

# ==================================================
# 2 Copy Image File
# ==================================================

source = open("image.jpg","rb")

data = source.read()

source.close()

target = open("image_copy.jpg","wb")

target.write(data)

target.close()

# ==================================================
# 3 Write Binary Data
# ==================================================

file = open("binary.dat","wb")

file.write(b"Hello Python")

file.close()

# ==================================================
# 4 Read Binary Data
# ==================================================

file = open("binary.dat","rb")

print(file.read())

file.close()