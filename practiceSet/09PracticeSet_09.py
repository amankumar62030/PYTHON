# WAP to find out wheather a file is identical & matches the content of another file

with open(r"D:\PYTHON\practiceSet\0908_copy.txt") as f:
    content1 = f.read()

with open(r"D:\PYTHON\practiceSet\0908.txt") as f:
    content2 =f.read()

if(content1 == content2):
    print("Yes these files are identical")
else:
    print("No, these files are not identical")