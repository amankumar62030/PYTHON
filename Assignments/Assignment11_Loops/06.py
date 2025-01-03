# Write a python script to calculate factorial of a given number

n = int(input("Enter the number: "))
fact = 1
for i in range(1,n+1):
    fact*=i
print(fact)