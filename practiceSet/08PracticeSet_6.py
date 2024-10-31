# WAP using function to convert inches to cms

n = int(input("enter your number:"))

def cm(n):
    return n*2.54

print(f"{n} inches is equal to {cm(n)}")