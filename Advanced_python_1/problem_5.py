n=int(input("Enter a Number :"))

l=[n*i for i in range (1,11)]
print(l)
with open("tables.txt","a") as f:
    f.write(f"Table of {n} : {str(l)} \n")

