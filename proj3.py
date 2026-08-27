a=input("give a sting with spaces in between")
n=len(a)
for i in range(0,n):
    if a[i]==" ":
        b+=a[i].replace(" ","")
    else:
        b+=a[i]

print(b)