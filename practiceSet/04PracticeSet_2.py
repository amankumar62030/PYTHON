# WAP to accept marks of 6 students and display them in a sorted manner

marks =[]

m1 = int(input("Enter the marks of 1st subject: "))
marks.append(m1)
m2 = int(input("Enter the marks of 2nd subject: "))
marks.append(m2)
m3 = int(input("Enter the marks of 3rd subject: "))
marks.append(m3)
m4 = int(input("Enter the marks of 4th subject: "))
marks.append(m4)
m5 = int(input("Enter the marks of 5th subject: "))
marks.append(m5)
m6 = int(input("Enter the marks of 6th subject: "))
marks.append(m6)

marks.sort()
print(marks)