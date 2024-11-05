# Wap to make a copy of a text file "this.txt"

with open(r"D:\PYTHON\practiceSet\0908.txt") as f:
    content =f.read()

with open(r"D:\PYTHON\practiceSet\0908_copy.txt", "w") as f:
    f.write(content)