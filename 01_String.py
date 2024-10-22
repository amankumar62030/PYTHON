name = "AMANKUMAR"

print(len(name))

nameshort = name[0 : 3] #start from the index 0 all the way till 3 (excluding 3)
print(nameshort)

character1 = name[1]
print(character1)


# A M A N K U M A R
# 0 1 2 3 4 5 6 7 8 
#-9-8-7-6-5-4-3-2-1
 
# Negative slicing
print(name[-8 : -5])
print(name[1 : 4])

print(name[:4]) #is same as print(name[0:4])
print(name[1:]) #is same as print(name[1:9]) means length


# Slicing with skip value
word = "amazing"
print(word[1 : 6 : 2]) #it will skip every 2nd letter in the given interval

