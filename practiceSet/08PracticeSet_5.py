# WAP using function to print following pattern
# n = 3
# ***
# **
# *

n = int(input("Enter your number:"))

def pattern(n):
    if(n == 0):
        return
    print("*" * n)
    pattern(n-1)

pattern(n)