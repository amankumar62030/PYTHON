#  Write a python script which takes a three digit number from the user and displays
#  only its middle digit.

n = int(input("Enter the three digit number: "))
digit = n//10
middle_digit = digit%10

print(middle_digit)