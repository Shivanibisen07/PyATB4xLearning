from operator import truediv, lshift

my_list = [1, 2, 'shivani', True]
print(len(my_list))
print(my_list[2])

my_list[1] = "Girrafe"

#print(my_list)
for element in my_list:
    print(element)

"""my_list.append("Arman",5,6,7,8)
print(my_list)"""

my_list.append("Arman")
print(my_list)

my_list.extend(["Cow",False, 33, 55])
print(my_list)

my_list.