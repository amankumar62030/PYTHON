# Write a python script to check whether a given number is Prime or not

n = int(input("Enter the number: "))

is_prime = True

for i in range(2,n):
    if n%i==0:
        is_prime=False
        break
if is_prime:
    print("PRime")
else:
    print("Not Prime")