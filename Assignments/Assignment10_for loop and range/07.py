# Write a python script to print first N odd natural numbers

n = int(input("Enter the number: "))

for i in range(1,n+1):
    if i%2!=0:
        print(i)