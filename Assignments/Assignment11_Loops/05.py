# Write a python script to calculate sum of first N even natural numbers


n = int(input("Enter the number: "))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
print(sum)