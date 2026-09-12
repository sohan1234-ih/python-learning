#expense tracker
import json
expense=[]
#with open("expense.json","r") as f:
#    expense.append(json.load(f))
n=int(input("How many expenses did you make today"))
i=1
while i<=n:
    expense.append({"name" : input(f"What is your {i} expense") , "amount" : int(input(f"The amount you spent on this:"))})
    i+=1

def view_exp():
    a=len(expense)
    i=1
    print("Expenses:")
    while i<=a:
        print(f"{expense[i-1]['name']} -- {expense[i-1]['amount']}")
        i+=1
def tot_exp():
    tot=0
    for i in range(0,len(expense)):
        tot+=expense[i]["amount"]
    print(f"Total : {tot} ")

with open("expense.json","w") as f:
    json.dump(expense,f)