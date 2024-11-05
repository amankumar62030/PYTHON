# WAP to find out the line number where python is present from ques 6.


with open(r"D:\PYTHON\practiceSet\0906.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("Python" in  line):
        print(f"Yes, Python exist. Line no. {lineno}")
        break
    lineno += 1
else:
    print("Python not exist")