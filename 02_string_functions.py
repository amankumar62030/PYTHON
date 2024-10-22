# String functions
# -------------------------------------



name = "Viratkohli"
print(len(name))

print(name.endswith("rry"))  #it will return false
print(name.endswith("hli"))  #it will return true
print(name.endswith("hLi"))  #it will return false

print(name.startswith("Vir"))  #it will return true
print(name.startswith("vir"))  #it will return false

word = "hell23o world"
print(word.capitalize()) #it only capitalize first letter 

print(word.isalnum())   #false
print(name.isalpha()) #true

print(word.islower())  #return true if all characters are in lowercase

print(word.upper())  #convert all the characters into uppercase

print(word.strip()) #It removes leading and trailing spaces in the string

