# Write a python script to print table of user’s choice

n = int(input("Enter the table no. u want to print: "))

for i in range(1,11):
    print(f"{n}X{i}={n*i}")