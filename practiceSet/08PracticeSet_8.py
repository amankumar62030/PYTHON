# WAP to print table

n = int(input("Enter your number:"))

def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

table(n)