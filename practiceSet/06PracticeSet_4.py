# WAP to find wheather a given username contains less than 10 characters or not.

username = input("Input the username: ")

length = len(username)


if length < 10:
    print("The username contains less than 10 characters.",length)
else:
    print("The username contains 10 or more characters.",length)


