try:
    m=int(input("Enter the first number:"))
except ValueError:
    print("Enter a valid number")
oper=input("Enter an opertion(+,-,*,/):")
try: 
    n=int(input("Enter the second number:"))
except ValueError:
    print("enter a valid number")
a=('+',"-","*","/")
if oper not in ("+",'-','*','/'):
    raise ValueError("give me a valid operation")


