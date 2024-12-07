# Write a python script to take the month value in numeric format and display the
#  number of days in it.

month = int(input("Enter the month in numeric format (1-12): "))

if month == 1:
    print("31 days")
elif month == 2:
    print("28/29 days (February)")
elif month == 3:
    print("31 days")
elif month == 4:
    print("30 days")
elif month == 5:
    print("31 days")
elif month == 6:
    print("30 days")
elif month == 7:
    print("31 days")
elif month == 8:
    print("31 days")
elif month == 9:
    print("30 days")
elif month == 10:
    print("31 days")
elif month == 11:
    print("30 days")
elif month == 12:
    print("31 days")
else:
    print("Invalid month! Please enter a value between 1 and 12.")
