students={ 101:{"name": "sohan","marks":98},
          102:{"name": "anushh","marks":89}}
def add_student():
    iden=int(input("Enter the student id number"))
    name=input("Enter the name of the student")
    mark=int(input("Enter the student\'s mark"))
    students.update({iden:{"name": name,"marks":mark}})

def find_student(id):
    if id not in students.keys():
        print("Error.Id not found")
    else:
        find=(students.get(id))
        print(f"The name of the student:{find["name"]}")
        print(f"The marks obtained by the student:{find["marks"]}")


def com_dis():
    for key, values in students.items():
        print(f"Student id:{key}")
        print(f"Student name:{values["name"]}")
        print(f"Marks obtained:{values["marks"]}")


com_dis()