# WAP which will keep addign a stream of numbers inputted by the user. The adding stops as soon as user presses q key on the keyboard

sum = 0
while(True):
    userInput = input("Enter the price: ")

    if(userInput!='q'):
        sum = sum+int(userInput)
    else:
        print(f"Your total bill is: {sum}")
        print("Thankyou, visit again")
        break

