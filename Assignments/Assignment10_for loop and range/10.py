# Write a python script to display all prime numbers within a range.
# # range
# start = 15
# end = 45

start=15
end=46
for i in range(start,end+1):
    is_prime = True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime and i>1:
        print(i)
