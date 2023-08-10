list1 = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]
print("List Before ", list1)
temp_list = []

for i in list1:
    if i not in temp_list:
        temp_list.append(i)

list1 = temp_list

print("List After removing duplicates ", list1)