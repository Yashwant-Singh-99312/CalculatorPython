# This is a calculator 
p = input("What is the first character?")
q = input("What is the Second character?")



operator = input("What would you like to do?")

if operator == "+":
    result = float(p) + float(q)
    print(result)

elif operator == "-":
    result = float(p) - float(q)
    print(result)        

elif operator == "x":
    result = float(p) * float(q)
    print(result)        

elif operator == "/":
    result = float(p) / float(q)
    print(result)
