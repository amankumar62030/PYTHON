# Write a python script to use NOT IN operator to display the data not present in list

my_list = [10, 20, 30, 40, 50]
check_list = [60, 70, 80] 

for i in my_list:
    if i not in check_list:
        print(i)