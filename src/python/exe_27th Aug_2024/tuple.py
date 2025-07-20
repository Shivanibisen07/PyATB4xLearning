my_urls = ("abc.com", "cvt", "etc.com")
print(my_urls)

my_list=list(my_urls)
print(my_list)

third_tuple = (my_urls,my_list)
print(third_tuple)

print(third_tuple[0][1])

cities = ("London","Paris","Italy")
print("London" in cities)
print("Newdelhi" in cities)