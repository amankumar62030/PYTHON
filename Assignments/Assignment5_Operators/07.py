#  Write a python script which takes a three digit number from the user and displays
#  only its last digit.

n = int(input("Enter the three digit number: "))
digit = n%10
print(digit)