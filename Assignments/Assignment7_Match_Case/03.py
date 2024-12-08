# Write a menu driven program with the following options:
#  a. Check whether a given set of three numbers are lengths of an isosceles
#  triangle or not
#  b. Check whether a given set of three numbers are lengths of sides of a right
#  angled triangle or not
#  c. Check whether a given set of three numbers are equilateral triangle or not
#  d. Exit.

while True:
    print("\nMenu:")
    print("a. Check for isosceles triangle")
    print("b. Check for right-angled triangle")
    print("c. Check for equilateral triangle")
    print("d. Exit")
    
    choice = input("Enter your choice (a/b/c/d): ").lower()

    match choice:
        case 'd':  # Exit
            print("Exiting program.")
            break
        
        case 'a' | 'b' | 'c':  # Handle triangle checks
            # Input the three numbers
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            num3 = int(input("Enter the third number: "))
            
            # Check triangle inequality
            if num1 + num2 <= num3 or num2 + num3 <= num1 or num1 + num3 <= num2:
                print("The numbers do not form a triangle.")
                continue
            
            match choice:
                case 'a':  # Check for isosceles triangle
                    if num1 == num2 or num2 == num3 or num1 == num3:
                        print("The numbers form an isosceles triangle.")
                    else:
                        print("The numbers do not form an isosceles triangle.")
                
                case 'b':  # Check for right-angled triangle
                    if (num1**2 + num2**2 == num3**2 or
                        num2**2 + num3**2 == num1**2 or
                        num1**2 + num3**2 == num2**2):
                        print("The numbers form a right-angled triangle.")
                    else:
                        print("The numbers do not form a right-angled triangle.")
                
                case 'c':  # Check for equilateral triangle
                    if num1 == num2 == num3:
                        print("The numbers form an equilateral triangle.")
                    else:
                        print("The numbers do not form an equilateral triangle.")
        
        case _:  # Handle invalid choices
            print("Invalid choice. Please choose a valid option.")
