# Write a python script to check whether a given number is Prime or not

n = int(input("Enter the number: "))

for i in range(2,n):
    if n%i==0:
        print("The number is not prime")
        break
    else:   
        print("The number is prime")        
