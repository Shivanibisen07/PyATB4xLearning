my_shopping_list=["bread", "butter","maggiee"]
print(my_shopping_list[0])
print(len(my_shopping_list))

def bring_more_item(my_list):
    more_items=input("Enter items\n")
    my_list.append(more_items)
    #my_list.remove("more_items")
    #my_list.insert(0,"milk")
    return my_list
l = bring_more_item(my_shopping_list)
print(l)

#To remove duplicte from the list --> set will be used