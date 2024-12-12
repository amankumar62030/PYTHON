# Write a python script to print first N even natural numbers

n = int(input("Enter the number: "))
i = 0
count = 0
while count < n:
    if i % 2 == 0:
        print(i)
        count += 1  
    i += 1
