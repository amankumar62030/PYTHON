# WAP to print multiplication table of n using for loop in reverse order

n = int(input("Enter the number: "))

for i in range(10, 0,-1):
    print(f"{n} X {i} = {n*i}")
