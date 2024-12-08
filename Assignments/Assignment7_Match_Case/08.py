#  Write a python script to check whether two given strings are identical, first string
#  comes before the second in dictionary order or first string comes after the second
#  string in dictionary order using match case statement


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

match True:
    case True if str1 == str2:
        print("The two strings are identical.")
    case True if str1 < str2:
        print(f'"{str1}" comes before "{str2}" in dictionary order.')
    case _:
        print(f'"{str1}" comes after "{str2}" in dictionary order.')

