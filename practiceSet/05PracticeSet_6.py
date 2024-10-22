# WAP to create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names. Assume that the names are unique.

d = {}

name = input("Enter Friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})
name = input("Enter Friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})
name = input("Enter Friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})
name = input("Enter Friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})


print(d)
