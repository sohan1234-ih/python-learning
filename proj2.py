n=int(input("Give the number to recive its table"))
t=int(input("Give me the lenght of the table"))
if n<=0 or t<=0:
    print("ERROR.The given two numbers must be greater then zero")
else:
    for i in range(0,t+1):
        print(f"{n} X {i} = {n*i}")
