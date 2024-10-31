# WAP to find wheather a given number is prime or not
n = int(input("Enter the number: "))

for i in range(2, n):
    if(n%i==0):
        print("Not a prime number: ",n)
        break
else:
    print("Number is Prime: ",n)


    