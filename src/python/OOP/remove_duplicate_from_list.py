original_list = [1,2,4,3,4,35,6,7,8]
new_list = []

for i in original_list:
    if i not in new_list:
        new_list.append(i)

print(original_list)
print(new_list)