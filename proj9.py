
with open("notes.txt","a") as f:
    f.write("hi raaa reee!!")
    f.write("name of the player\n")
    f.write("level of the player\n")
    f.write("health of the player\n")

f.close
with open("notes.txt","r") as f:
    result=f.read()
print(result)