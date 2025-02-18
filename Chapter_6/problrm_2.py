marks1=float(input("Enter The Marks : "))
marks2=float(input("Enter The Marks : "))
marks3=float(input("Enter The Marks : "))

total_percentage=((marks1+marks2+marks3)/300)*100

if((marks1>=33 and marks2>=33 and marks3>=33) and total_percentage>=40):
    print("You Have Passed")
    print("Your Percentage",total_percentage)
else:
    print("Better Luck Next Time")
