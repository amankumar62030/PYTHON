#  Write a python script to print first N odd natural numbers

n = int(input("Enter the number: "))
i = 0
while i <= n:
    if i%2!=0:
        print(i)
    i+=1