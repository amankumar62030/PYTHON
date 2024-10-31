age = int(input("Enter the age: "))

if(age >= 18):
    print("Can Vote")
    print("Congrats")

elif(age < 0):
    print("Invailed age")
    
else:
    print("Can't Vote")