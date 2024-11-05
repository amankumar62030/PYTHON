# WAP to mine a log file and find out wheather it contains 'python'

with open(r"D:\PYTHON\practiceSet\0906.txt") as f:
    content = f.read()

if("python" in  content or "Python" in content):
    print("Yes, Python exist")
else:
    print("Python not exist")