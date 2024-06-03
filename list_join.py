#join two list
list_1 = ["a", "b", "c"]
list_2 = [1,2,3]

list_3 = list_1 + list_2
print(list_3)

#append list2 into list1
list_1 = ["a", "b", "c"]
list_2 = [1, 2, 3, 4]

for x in list_2:
    list_1.append(x)

print(list_1)   


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)