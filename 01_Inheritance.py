class Employee:
    company = "ITC"
    name = "Default"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")


class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all languages here is your language: {self.language}")


# class Programmer:
#     company = "ITC INFOTECH"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good in language {self.language}")


# ...........We use Inheritence...........
class Programmer(Employee,Coder):
     company = "ITC INFOTECH"
     def showLanguage(self):
        print(f"The name is {self.company} and he is good in language {self.language}")




a = Employee()
b = Programmer()

# print(a.company, b.company)
b.show()
b.printLanguages()
b.showLanguage()