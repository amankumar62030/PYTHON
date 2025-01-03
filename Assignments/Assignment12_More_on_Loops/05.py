# Write a python script to find next prime number of a given number

n = int(input("Enter the number: "))

for i in range(n+1,10000):
    is_prime = True
    for j in range(2,i):
        if i%j==0:
            is_prime = False
    if is_prime:
        print(i,end=' ')
        break

    

