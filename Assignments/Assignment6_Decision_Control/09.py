# Write a python script to check whether a given year is a leap year or not.

year = int(input("Enter the year: "))

if year%400==0:
    print("Leap year")
elif year%100==0:
    print("Not a leap year")
elif year%4==0:
    print("Leap year")
else:
    print("Not a leap year")
    