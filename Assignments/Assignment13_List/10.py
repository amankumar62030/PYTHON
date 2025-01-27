#  Write a Python script to create a list, where each element of the list is a digit of a
# given number

number = input("Enter the number: ")

list_digit =[]

for i in number:
    list_digit.append(int(i))

print(list_digit)