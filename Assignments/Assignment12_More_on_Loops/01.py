# Write a python script to reverse a number.


n = int(input("Enter the number: "))
rev_no = 0

while n>0:
    rem = n%10
    rev_no = rev_no*10+rem
    n=n//10
print(rev_no)