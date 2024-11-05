class Employee:
    language = "Python"
    salary = 120000

    def __init__(self, name, salary, language):    #dunder method which is automatically call
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry = Employee("Harry", "1322000", "JavaScript")
harry.name = "harry"
print(harry.name, harry.salary, harry.language)