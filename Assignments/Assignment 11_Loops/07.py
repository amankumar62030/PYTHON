# Write a python script to count digits in a given number

n = int(input("Enter the number: "))
count = 0
for i in str(abs(n)):
    count+=1
print(count)