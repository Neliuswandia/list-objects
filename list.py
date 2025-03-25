# empty list 
my_list = []
 
#  appending into a list
new_list = [10, 20, 30, 40]

for x in new_list:
    my_list.append(x)

# inserting into a list as per the index
my_list.insert(1, 15)

# extending my list
my_list.extend([50,60,70])

# removing the last element
my_list.pop()

# sorting my list in an ascending order
my_list.sort(reverse=True)

# printing the value of a given index from my list
print(my_list[3])

print(my_list)