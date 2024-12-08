#  Write a python script to check whether a given year is
#  a. Non century leap year
#  b. Century leap year
#  c. Non century non leap year
#  d. Century non leap year


year = int(input("Enter the year: "))

match year:
    case year if year%400==0:
        print("Century leap year.")
    case year if year%100==0 and year%400!=0:
        print("Century non-leap year.")
    case year if year%4==0 and year%100!=0:
        print("Non-century leap year.")
    case _:
        print("Non-century non-leap year.")