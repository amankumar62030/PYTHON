class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

aman = Employee()
aman.language = "Java"
aman.getInfo()
aman.greet()
Employee.getInfo(aman)