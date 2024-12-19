# Write a python script to print binary equivalent of a given decimal number. (do not
# use bin() method)

decimal_num = int(input("Enter the number: "))

if decimal_num==0:
    print("The binary equivalent of 0 is 0")
else:
    binary=""
    while decimal_num>0:
        rem = decimal_num%2
        binary = str(rem)+binary
        decimal_num//=2
print(binary)