# A spam comment is defined as a text containing following keywords:
# "make a lot of money", "buy now", "subscribe this", "click this". WAP to detect this spams


p1 = "make a lot of money" 
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

msg = input("Enter your comment : ")

if(p1 in msg or p2 in msg or p3 in msg or p4 in msg):
    print("Its a spam")
else:
    print("Its not a spam")
