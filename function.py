def add(a,*b):
 print(a,b)
add(2,4,7)

# def user_input_to_dictionary():
#     user_dict = {}
#     while True:
#         key = input("Enter a key (or press Enter to finish): ")
#         if not key:
#             break
#         value = input("Enter a value: ")
#         user_dict[key] = value
#     return user_dict

# # Example usage:
# user_data = user_input_to_dictionary()
# print("User's dictionary:", user_data)



def user(**a):
    a = int(input("Enter a Number"))
    print(a)

user()

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# a = ["A","B","C"]

# my_function(fruits)
# my_function(a)


# def process_dictionary(input_dict):
#     for key, value in input_dict.items():
#         print(f"Key: {key}, Value: {value}")

# # Example usage:
# # my_dict = {"name": "Qavi", "age": 19, "city": "hyderabad"}

# process_dictionary(my_dict)

# def create_dictionary_from_user_input():
#     user_dict = {}
#     while True:
#         key = input("Enter a name (or press Enter to finish): ")
#         if not key:
#             break
#         value = input("Enter CNIC: ")
#         user_dict[key] = value

#     return user_dict

# # Example usage:
# user_data = create_dictionary_from_user_input()
# print("User's dictionary:", user_data)


# def tri_recursion(k):
#   if(k > 0):
#     result = k * tri_recursion(k * 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(9)

# def factorial(n):
#     if n == 0:
#         return 0
#     else:
#         return n * factorial(n - 1)

# n = 3  # Change this to the desired number
# result = factorial(n)
# print(f"The factorial of {n} is {result}")



# q = lambda a : a*10
# a = int(input("enter a number"))
# f= q(a)
# print(f)


# h = lambda c,d,e : c+d+e
# p = h(5,5,5)
# print(p)

add = lambda a , b : a + b
sub = lambda a , b : a - b
mul = lambda a , b : a * b
div = lambda a , b : a / b
# exp = lambda a , b : (a((a + b)/(a-b)))

A = add(5,5)
S = sub(10,5)
M = mul(5,5)
D = div(5,5)
# E = exp(10,5)
print(A)
print(S)
print(M)
print(D)
# print(E)

x = 10
y = 5
exp = mul(x,(div(add(x,y),sub(x,y))))
print(exp)


# a = 5
# b = 10
# a((a + b)/(a-b))
# 30

# x = lambda d,e : d+e
# d = int(input("Enter first"))
# e = int(input("Enter second"))
# ad = x(d,e)
# print(ad)

