# Write a menu driven program to perform following operations - Addition, Subtraction,
#  Multiplication, Division

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

n = int(input("Choose the operation you want to perform(1,2,3 and 4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

match n:
    case 1: 
        print(f"The sum is {num1+num2}")
    case 2:
        print(f"The subtraction is : {num1-num2}")
    case 3:
        print(f"Multiplication is : {num1*num2}")
    case 4:
        print(f"Division is : {num1/num2}")
    case other:
        print("Enter valid input")


