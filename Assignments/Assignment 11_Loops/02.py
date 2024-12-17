# Write a python script to calculate sum of squares of first N natural numbers

n = int(input("Enter the number: "))
sum=0
for i in range(1,n+1):
    sum+=i**2
print(sum)