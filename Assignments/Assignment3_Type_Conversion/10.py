#  Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
#  display the result in binary format

a = 25
b = oct(a)
print(b)
c = 39
d = hex(c)
print(d)

result_b = int(b,8)
result_d = int(d,16)

result = result_b+result_d

print(f"{bin(result)}")
