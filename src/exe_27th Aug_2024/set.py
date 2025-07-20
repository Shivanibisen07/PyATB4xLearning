list_of_unique_items = {1,2,3,3,4,4,5,6}
print(list_of_unique_items)

list1 = [45.3,33,6,7,7,8]
set1=set(list1)
print(set1)

set2 = {3,4,5}
set3 = {6,7,8}
my_set = set2.union(set3)
print(my_set)
my_new_set = set1.intersection(set3)
print(my_new_set)