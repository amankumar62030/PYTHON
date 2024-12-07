# Write a python script to print two given words in dictionary order

wrd1 = input("Enter first word: ")
wrd2 = input("Enter second word: ")

# Compare the words and print in dictionary order
if wrd1 < wrd2:
    print(wrd1)
    print(wrd2)
else:
    print(wrd2)
    print(wrd1)
