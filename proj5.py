student1=set()
student2=set()
n=int(input("Enter the number of subjects taken by student 1:"))
m=int(input("Enter the number of subjects taken by student 2:"))
for i in range(0,n):
    student1.add(input("enter the subjects").lower())
for i in range(0,m):
    student2.add(input("enter the subjects").lower())

print(f"The total subjects are:{student1|student2}")
print(f"The common subjects are:{student1&student2}")
