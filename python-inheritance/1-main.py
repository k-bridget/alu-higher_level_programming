#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

# Print original list
print(my_list)

# Print sorted list
my_list.print_sorted()

# Print the original list again to ensure it is unchanged
print(my_list)

