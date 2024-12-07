#  Write a python script to print greater among three numbers. Print number only once
#  even if the numbers are the same.

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 >= n2 and n1 >= n3:
    print(f"{n1} is greater")
elif n2 >= n3 and n2 >= n1:
    print(f"{n2} is greater")
else:
    print(f"{n3} is greater")
    