# Repeat program 4 for a list of such words to be censored.

words = ["cat", "quiet", "quietly", "moment"]

with open(r"D:\PYTHON\practiceSet\0905.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open(r"D:\PYTHON\practiceSet\0905.txt", "w") as f:
    f.write(content)