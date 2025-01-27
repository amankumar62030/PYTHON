# Write a Python script to create a list of city names taken from the user.

city =[]
length = int(input("Enter how many city u want to print: "))
for i in range(length):
    city_name = input("Enter the city name: ")
    city.append(city_name)

print("List of cities are: ", city)