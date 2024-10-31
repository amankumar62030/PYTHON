# WAP to calculate the grade of a student from his marks 

m = int(input("Enter the marks of the student: "))

if(m>=90 and m<=100):
    print("Excellent: ",m)
elif(m>=80 and m<90):
    print("Grade A: ",m)
elif(m>=70 and m<80):
    print("Grade B: ",m)
elif(m>=60 and m<70):
    print("Grade C: ",m)
elif(m>=50 and m<60):
    print("Grade D: ",m)
else:
    print("Fail: ",m)