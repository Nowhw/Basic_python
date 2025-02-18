a=int(input("Enter A Number :"))
b=int(input("Enter A Number :"))
c=int(input("Enter A Number :"))

def greatest(a,b,c):
    if(a>b and a>c):
        print(f"A= {a} is the greatest number")
    elif(b>a and b>c):
        print(f"B= {b} is the greatest number")
    else:
        print(f"C= {c} is the greatest number")




greatest(a,b,c)