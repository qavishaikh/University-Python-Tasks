# Create a tuple named my_tuple
my_tuple = ("apple", 5, 2.5)

print(my_tuple)

for x in my_tuple:
    print(x)

second = my_tuple[1]
print(second)

# Create a tuple named coordinates representing (x, y, z) coordinates
coordinates = (3.5, 2.0, -1.5)

# Print the tuple
print("Coordinates:", coordinates)

# Create a tuple named person with three elements
person = ("Qavi", 30, "Engineer","Hyd")

# Use tuple unpacking to assign values to variables
name, age, occupation, city = person

# Print the values of the variables
print("Name:", name)
print("Age:", age)
print("Occupation:", occupation)
print("City:", city)

for Y in person:
    print(Y)


# Initial values
a = 5
b = 10

print("Before Swipiing")
print("A = ",a)
print("B = ",b)
# Swap the values using tuple packing and unpacking
a, b = b, a

# Print the swapped values
print("After swapping:")
print("A =", a)
print("B =", b)


# Create a tuple of numbers from 1 to 10
numbers_tuple = tuple(range(1, 11))

# Use tuple slicing to print elements from index 2 to 5
sliced_elements = numbers_tuple[0:5]

# Print the sliced elements
print("Sliced Elements:", sliced_elements)


# Create a tuple of characters representing the alphabet
alphabet_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z')

# Use slicing to print the last 5 characters
last_five_characters = alphabet_tuple[-5:]

# Print the last five characters
print("Last Five Characters:", last_five_characters)


# Create a tuple of integers
numbers_tuple = (2, 4, 6, 2, 8, 10, 2, 12, 14, 2)

# Specify the element you want to count
element_to_count = 2

# Use the count() method to count the element
count_of_element = numbers_tuple.count(element_to_count)

# Print the count
print(f"The element {element_to_count} appears {count_of_element} times in the tuple.")


# Create a tuple of names
names_tuple = ("Ali", "Hamdan", "Nadeem", "Qavi", "Fizan", "Saad")

# Specify the name you want to find
name_to_find = "Qavi"

# Use the index() method to find the index of the name
index_of_name = names_tuple.index(name_to_find)

# Print the index
print(f"The index of '{name_to_find}' in the tuple is {index_of_name}.")


# # Create a tuple
# my_tuple1 = (1, 2, 3)

# # Attempt to modify an element (this will result in an error)
# my_tuple1[1] = 10

# Create a tuple containing the squares of even numbers from 1 to 10
squares_of_even_numbers = tuple(x**2 for x in range(1, 22) if x % 2 == 0)

# Print the tuple
print(squares_of_even_numbers)
