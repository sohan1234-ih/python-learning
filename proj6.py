sen=input("Enter a sentence:")
n=len(sen)
vov=0
con=0
space=0
for i in range(0,n):
    if sen[i] in ("a","e","i",'o','u'):
        vov+=1
    if sen[i] not in ("a",'e','i','o','u',' '):
        con+=1
    if sen[i] in (" "):
        space+=1
print(f"The number of vowels are:{vov}")
print(f"The number of consonents are:{con}")
print(f"The number of characters are:{n}")
fin=input("enter the word you are looking for")
if fin in sen:
    print(f"{fin} is found")
else:
    print(f"{fin} not found")