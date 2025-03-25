# empty list 
my_list = []
 
#  appending into a list
new_list = [10, 20, 30, 40]

for x in new_list:
    my_list.append(x)

# inserting into a list as per the index
my_list.insert(1, 15)

my_list.extend([50,60,70])

print(my_list)