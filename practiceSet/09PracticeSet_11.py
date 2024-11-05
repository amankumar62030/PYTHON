# WAP to rename a file to "renamed_by_python.txt"

with open(r"D:\PYTHON\practiceSet\old.txt") as f:
    content = f.read()

with open(r"D:\PYTHON\practiceSet\renamed_by_Python.txt", "w") as f:
    f.write(content)