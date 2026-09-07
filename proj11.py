import json

student = {
    "name": "Sohan",
    "age": 18,
    "course": "Mechanical Engineering"
}

data = json.dumps(student)

print(data)