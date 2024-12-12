# Write a python script to print first 10 odd natural numbers

i = 1
count = 0
while count < 10:
    if i%2!=0:
        print(i,end=" ")
        i+=2
        count+=1