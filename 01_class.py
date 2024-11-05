class Employee:
    language = "Python"    #this is the class attributes
    salary = 1200000


aman = Employee()
aman.name = "aman"
print(aman.name, aman.language, aman.salary)

rohan = Employee()
rohan.name = "rohan"    #this is the instance(object) attribute
print(rohan.name, rohan.salary, rohan.language)



# Here name is instance(object) attribute and salary and language are class attributes as they directly belongs to the class

