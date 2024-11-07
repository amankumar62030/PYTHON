class Employee:
    a = 1
    @classmethod   #it prints the value 1 not 43
    def show(cls):
        print(f"The class value of a is {cls.a}")

e = Employee()
e.a = 43

e.show()