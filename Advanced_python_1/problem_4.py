try:
    a=int(input("Enter A Number :"))
    b=int(input("Enter Another Number :"))

    print(f"{a/b}")

except ZeroDivisionError as z:
    print("Infinite")
