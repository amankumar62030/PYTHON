# Write a python script to print first 10 multiples of N

n =int(input("Enter the number: "))
i = 1
count = 0
while count < 10:
    if i%n==0:
        print(i,end=" ")
        count+=1
    i+=1
