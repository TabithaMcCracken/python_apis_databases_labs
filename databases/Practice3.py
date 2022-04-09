list_1 = [1,2,3,4]
list_2 = [1,5,6,7]

new_list = list(set(list_1).difference(list_2))
print(new_list)

new_list2 = list(set(list_2).difference(list_1))
print(new_list2)