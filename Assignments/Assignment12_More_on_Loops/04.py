# Write a python script to print all Prime numbers between two given numbers (both
# values inclusive)
start = int(input("Enter the number: "))
end = int(input("Enter the second number: "))

for i in range(start,end+1):
    is_prime = True

    for j in range(2,i):
        if i%j==0:
            is_prime = False
            break
    if is_prime:
        print(i,end=' ')