a = (1, 34.5, 45, 45, False, "Rohan", "Shivam")

no = a.count(45)  #return no. of times 45 occurs
print(no)

i = a.index(34.5)
print(i)

#concatination
t1 = (1,2,3)
t2 = (4,5,6)
concat = t1 + t2
print(concat)
print(len(concat))

print(2 in t1) #return true
print(4 in t1) #return false

# min and max
print(min(concat))
print(max(concat))