n=int(input("Enter The NUmber Of Rows :"))

# def pattern(n):
#     for i in range(0,n):
#         print("*"*(n-i),end="")
#         print(" ")

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

pattern(n)