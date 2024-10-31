age = int(input("Enter the age: "))

# if elif ladder

if(age >= 18):
    print("Eligible to vote")

elif(age < 18):
    print("Not eligible to vote")

elif(age < 0):
    print("Enter valid age")
else:
    print("Cannot determined")