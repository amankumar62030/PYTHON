'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2X1
factorial(3) = 3X2X1
factorial(4) = 4X3X2X1
factorial(5) = 5X4X3X2X1

factorial(n) = n X n-1 X............3 X 2 X 1

factorial(n) = n * factorial(n-1)
'''

n = int(input("Enter the number: "))

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n-1)

result = factorial(n)
print(result)








# ...........................................................
# n = int(input("enter the number:"))
# fact = 1
# for i in range(1,n+1):
#     fact*=i

# print(fact)