#calculate the factorial of a agiven number
#find the number of trailing zeros in that factorial


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact

n = int(input("Enter any number: "))
result = factorial(n)
print(result)

def factorialTrailingZeros(n):
    pass