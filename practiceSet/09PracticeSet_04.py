# A file contains a word "Donkey" multiple times. you need to WAP which replace this word with #### by updating the sawe file.


word = "Donkey"

with open(r"D:\PYTHON\practiceSet\0904.txt") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open(r"D:\PYTHON\practiceSet\0904.txt", "w") as f:
    f.write(contentNew)