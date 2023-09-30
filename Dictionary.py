my_dict = {}
print(my_dict)

my_dict["Apple"] = 400
my_dict["Mango"] = 200
my_dict["Banana"] = 300
my_dict["Grapes"] = 100
my_dict["Orange"] = 500

print(my_dict)
my_dict["Apple"] = 1500
print("Updated",my_dict)
removes = my_dict.pop('Orange')
print("Deleted",removes)
print(my_dict)

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for keys,value in my_dict.items():
    print(keys,value)


# Check if a specific key exists using the 'in' keyword
key_to_check = 'Mango'

if key_to_check in my_dict:
    print(f"'{key_to_check}' exists in my_dict.")
else:
    print(f"'{key_to_check}' does not exist in my_dict.")

# List of fruits
fruits = ['apple', 'banana', 'orange', 'strawberry', 'kiwi']

# Create a dictionary mapping fruit names to their lengths using a dictionary comprehension
fruit_lengths = {fruit: len(fruit) for fruit in fruits}

# Print the resulting dictionary
print(fruit_lengths)
