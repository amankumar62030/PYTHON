# WAp to read the text from a given file 'poems.txt' and find out wheather it contains the word 'twinkle'.

with open("D:\PYTHON\practiceSet/poems.txt") as f:
    content = f.read()
    
    if("twinkle" in content):
        print("Yes twinkle is present in the content")
    else:
        print("Twinkle is not present in the content")
    