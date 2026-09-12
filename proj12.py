import csv
with open("student.csv","w") as file:
    writer = csv.DictWriter(file,fieldnames=["name","age","course"])
    writer.writerow(
        {
            "name":"sohan","age":"18","course":"mechanical engineering"
        })
