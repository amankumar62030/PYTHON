a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Check if it's a quadratic equation
if a == 0:
    print("This is not a quadratic equation.")
else:
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Determine the nature of the roots
    if discriminant > 0:
        print("The equation has two real and distinct roots.")
    elif discriminant == 0:
        print("The equation has two real and equal roots.")
    else:
        print("The equation has imaginary roots.")
