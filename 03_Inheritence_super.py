class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class manager(Programmer):
    def __init__(self):
        super().__init__()  #yeh apne parent ka constructor bi chala dega
        print("Constructor of manager")
    c = 3

# o = Employee()
# print(o.a) 

# o = Programmer()
# print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)