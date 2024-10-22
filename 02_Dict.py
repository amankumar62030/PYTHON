marks = {
    "Harry" : 100,
    "Aman" : 98,
    "Shubham" : 59,
    0 : "Harrpy"
}

print(marks)

print(marks.items())
print(marks.keys())
print(marks.values())

#Dictionary is mutable so marks of harry will be updated
#Renuka will be added if it not exist
marks.update({"Harry":93, "Renuka":44})
print(marks)

# If we use get then if the key does not exist in the dictionary it gives NONE
print(marks.get("Harry"))
# If we use this bracket and if key does not exist then it gives error
print(marks["Harry2"])

