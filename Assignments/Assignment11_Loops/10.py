# Write a python script to print the octal equivalent of a given decimal number. (do not
# use oct() method)

decimal_num = int(input("Enter the number: "))

if decimal_num==0:
    print("The octal equivalent of 0 is 0")
else:
    octal=""
    while decimal_num>0:
        rem = decimal_num%8
        octal = str(rem)+octal
        decimal_num//=8
print(octal)