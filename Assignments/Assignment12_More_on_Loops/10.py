# Write a python script to calculate HCF of two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1>num2:
    mn=num2
else:
    mn = num1

for i in range(1,mn+1):
    if(num1%i==0 and num2%i==0):
        hcf = i



