def add(a,b):
    result=a+b
    print(result)

def sub(a,b):
    result=a-b
    print(result)

def mul(a,b):
    result=a*b
    print(result)

def div(a,b):
    result=a/b
    print(result)

a=int(input("Enter a number: "))
b=int(input("Enter a second number: "))
op=input("Enter an operator: ")

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="/":
    div(a,b)
else:
    print("Give a valid operator")