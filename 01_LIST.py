# Python lists are the containers to store a set of values of any data type.

name = ["Apple", "Orange", 5, 345.3, False, "Aakash", "Aman"]

print(name)
print(name[0])
print(name[3])

# List is mutable we can modify the value
name[1] = "Grapes"
print(name[1])
print(name)
print(name[1 : 4])  #slicing