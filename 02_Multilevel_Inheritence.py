class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class manager(Programmer):
    c = 3

o = Employee()
print(o.a) #prints the a attributes
# print(o.b) #shows an error as there is no b attributein employee class


o = Programmer()
print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)