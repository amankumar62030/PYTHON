# Write a program to display day name on the basis of user’s liking of a colour. Ask
#  user for his favorite colour. User can answer in a sentence like “I like red colour”.
#  Assuming all colour name entered by user is in lowercase. Use match case to display
#  day name associated with the colour.
#  a. Yellow - Monday
#  b. Blue - Tuesday
#  c. Orange - Wednesday
#  d. White - Thursday
#  e. Black - Friday
#  f.Red - Saturday
#  g. All other colours - Sunday

fav_clr = input("Enter your favourite colour: ").lower()

match fav_clr:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thursday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case others:
        print("Sunday")
