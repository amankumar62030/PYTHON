# Write a python script to print first N even natural numbers in reverse order

n = int(input("Enter the number: "))
i = 2 * n  # Start from the largest even number in the first N even numbers

while i > 0:
    print(i)
    i -= 2  # Move to the next smaller even number
