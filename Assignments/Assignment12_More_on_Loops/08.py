# Write a python script to print first N terms of a Fibonacci series

n = int(input("Enter the number: "))

f = 0
s = 1

count = 0

while count < n:
    print(f, end=" ")
    temp = f + s
    f = s
    s = temp
    count += 1
