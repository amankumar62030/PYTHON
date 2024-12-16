# Write a python script to display all prime numbers within a range.
# # range
# start = 15
# end = 45

for num in range(15,46):
    is_prime =True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime and num>1:
        print(num)


