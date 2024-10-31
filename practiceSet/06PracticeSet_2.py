# WAP to find out wheather a student has passed or failed if it requires a total of 40% and atleast 33% in each subject to pass. Assume 3 subjects and take marks as input from the user.

sub1 = int(input("Enter the marks of sub 1: "))
sub2 = int(input("Enter the marks of sub2: "))
sub3 = int(input("Enter the marks of sub3: "))

# check for total percentage

per = ((100)*(sub1+sub2+sub3)/300)

if(per >= 40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("you are pass: ",per)

else:
    print("You fail: ",per)