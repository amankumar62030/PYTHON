# Write a python script to print first N prime numbers

n = int(input("Enter the number: "))

for i in range(1,n+1):
    is_prime = True

    for j in range(2,i):
        if i%j==0:
            is_prime = False
            break
    if is_prime:
        print(i,end=' ')