# Wap to generate a random number and asks the user to guess it.

# If the Player guess is higher than the actual number, the program displays "Lower number please". Similarly, if the users guess is too low, the program prints "higher number please". When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.format


import random

num = random.randint(1,101)
# print(num)
count = 0

while True:
    n = int(input("Enter the number between 1 to 100:"))
    count+=1

    if n == num:
        print(f"Congrats, You guessed right number in step {count}")
        break
    elif n > num:
        print("Lower number please")
    else:
        print("Higher number please")