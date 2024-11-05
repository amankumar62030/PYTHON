# WAP to create a class "programmer" for storing information of few programmers working at Microsoft

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("Harry", 120000, 253772)
print(p.name, p.salary, p.company, p.pincode)

r = Programmer("Rohan", 210000, 170303)
print(r.name, r.salary, r.company, r.pincode)