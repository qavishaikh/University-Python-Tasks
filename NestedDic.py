# Create a nested dictionary
my_dict = {
    'person1': {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    },
    'person2': {
        'name': 'Bob',
        'age': 25,
        'city': 'Los Angeles'
    },
    'person3': {
        'name': 'Charlie',
        'age': 35,
        'city': 'Chicago'
    }
}

# Access values using loops
for person_key, person_info in my_dict.items():
    print(f"Person: {person_key}")
    for key, value in person_info.items():
        print(f"{key}: {value}")
    print()

for person_key, person_info in my_dict.items():
    print(f"Person: {person_key}")

print()

for person_key, person_info in my_dict.items():
    print(f"Person: {person_key} and {person_info}")