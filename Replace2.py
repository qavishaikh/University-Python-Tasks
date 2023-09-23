print("\n Example 6")
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)  
print(my_list)  

print("\n Example 7")
my_list1 = [1, 2, 3, 4, 5]
my_list1[1:4] = [7, 8, 9]  # Replace elements at index 1, 2, and 3
print(my_list1)  # Output: [1, 7, 8, 9, 5]

print("\n Example 8")
my_list2 = [1, 2, 3, 4, 5]
replaced_item = my_list.pop(2)  # Remove and get the third element (3)
my_list2.insert(2, 6)  # Replace it with 6
print(my_list2)  # Output: [1, 2, 6, 4, 5]
