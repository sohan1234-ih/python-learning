import json

student = {
    "name": "Sohan",
    "age": 18,
    "course": "Mechanical Engineering"
}

data = json.dumps(student)

print(data)

result=json.loads(data)
print(result)
print(result["name"])