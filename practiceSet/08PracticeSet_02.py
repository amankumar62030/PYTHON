# WAP using function to convert celsius to fahrenheit

n = int(input("Enter temperature in Celsius:"))

def temp(n):
    f = n*(9/5)+32
    return f

print(temp(n))