import json

# ==================================================
# 1 Write JSON
# ==================================================

data = {
    "name":"Prachi",
    "age":22
}

with open("student.json","w") as file:

    json.dump(data,file)

# ==================================================
# 2 Read JSON
# ==================================================

with open("student.json","r") as file:

    data = json.load(file)

print(data)

# ==================================================
# 3 Dictionary To JSON String
# ==================================================

data = {
    "name":"Prachi",
    "age":22
}

json_data = json.dumps(data)

print(json_data)

# ==================================================
# 4 JSON String To Dictionary
# ==================================================

json_string = '{"name":"Prachi","age":22}'

data = json.loads(json_string)

print(data)

# ==================================================
# 5 Pretty JSON
# ==================================================

print(json.dumps(data,indent=4))