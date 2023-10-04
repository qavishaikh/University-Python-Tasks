setA = {1,2,3,4,5}
setB = {4,5,6,7,8}
resA = setA.union(setB)
resB = setA.intersection(setB)
resC = setA.difference(setB)
print("Union",resA)
print("Intersaction",resB)
print("Difference",resC)

for x in resA:
    print(x)

# Define two sets, A and B
A = {1, 2, 3,4,5}
B = {1, 2, 3, 4, 5}

# Check if A is a subset of B
is_subset = A.issubset(B)

# Print the result
if is_subset:
    print("A is a subset of B")
else:
    print("A is not a subset of B")


# Create a set containing the letters of "banana"
word_set = set("banana")

word_set.add('s')
print(word_set)

other_set = {'a', 'p', 's', 'e', 'l'}

symmetric_diff = word_set.symmetric_difference(other_set)

print("Symmetric Difference:", symmetric_diff)


# Define two sets, A and B
A = {1, 2, 3}
B = {'a', 'b', 'c'}

# Compute the Cartesian product using a list comprehension
cartesian_product = {(a, b) for a in A for b in B}

# Print the Cartesian product
for pair in cartesian_product:
    print(pair)
