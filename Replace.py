# Replace Methods in List
print("\n Example 1")
list = ["1","2","3","4","5"]
list[1] = "8"
list[2] = "99"
print(list)

print("\n Example 2 ")
list1 = ["A","B","C"]
a = list1.index("B")
list1[a] = "Q"
print(list1)

print("\n Example 3 ")
list2 = ["a","b","c","d"]
index = 0
while index < len(list2):
    if list2[index] == "a":
        list2[index] =  "q"
    index += 1
print(list2)

print("\n Example 4 ")
list3 = ["A","B","C","D","E"]
for index,value in enumerate(list3):
    if value == "D":
        list3[index] = "Q"
print(list3)

print("\n Example 5 ")
list4 = [1,2,3,4,5]
list4 = [66 if item == 3 else item for item in list4]
print(list4)
