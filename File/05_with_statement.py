f = open(r"D:\PYTHON\File\file.txt")

print(f.read())

f.close()

# The same can be written using the "with" statement like this:

with open(r"D:\PYTHON\File\file.txt") as f:
    print(f.read())

# you dont have to explicitly close the file