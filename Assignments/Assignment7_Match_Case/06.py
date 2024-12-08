# Write a python program to check whether a given string is a multiword string or single
#  word string using match case statement


user_input = input("Enter any string: ").strip()

match " " in user_input:
    case True:
         print("The given string is a multiword string.")
    case False:
        print("The given string is a single-word string.")