#  Write a python script to print greater between two numbers. Print number only once
#  even if the numbers are the same.

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if n1>n2:
    print(f"{n1} is greater")
else:
    print(f"{n2} is greater")