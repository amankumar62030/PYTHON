#no repeatation allowed
s = {1, 5, 43, 6, 5, 5, 7, 1, "Harry"}
print(s, type(s))

s.add(566)
print(s, type(s))

print(len(s))
s.remove(1)
print(s)