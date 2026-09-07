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
with open("student.json","w") as f:
    json.dump(student,f)
with open("student.json","r") as f:
    test=json.load(f)
print(test)