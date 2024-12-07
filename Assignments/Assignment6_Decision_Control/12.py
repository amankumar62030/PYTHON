# Write a python script to accept one complex number from the user and display the
#  greater number between real part and imaginary part

comple_number = complex(input("Enter the complex number: "))

real_part = comple_number.real
img_part = comple_number.imag

if real_part > img_part:
    print(f"{real_part}")
else:
    print(f"{img_part}")
