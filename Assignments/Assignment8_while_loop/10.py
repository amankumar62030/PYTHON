# Write a python script to print first 10 multiples of 5

i = 1
count = 0
while count < 10:
    if i%5==0:
        print(i,end=" ")
        count+=1
    i+=1