#  Write a python script to check whether a given number is a three digit number or not.

n = int(input("Enter the number: "))

if n<1000 and n>99:
    print("Its a three digit number.")
else:
    print("Not a three digit number.")