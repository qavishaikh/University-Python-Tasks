# Input list of numbers with duplicates
numbers_list = [2, 3, 5, 2, 7, 8, 5, 1, 3, 9]

unique_numbers_set = set(numbers_list)

unique_numbers_list = list(unique_numbers_set)

print("List with Duplicates Removed:", unique_numbers_list)



def power_set(input_set):
    # If the input set is empty, the only subset is the empty set
    if not input_set:
        return [set()]

    # Get the first element of the set
    first_element = next(iter(input_set))

    # Recursively compute the power set for the set without the first element
    subsets_without_first = power_set(input_set - {first_element})

    # Add the first element to each subset in the subsets_without_first
    subsets_with_first = [{first_element} | subset for subset in subsets_without_first]

    # Combine both subsets to get the final power set
    return subsets_without_first + subsets_with_first

# Test the power_set function
input_set = {1, 2, 3}
result = power_set(input_set)

# Print the power set
for subset in result:
    print(subset)
