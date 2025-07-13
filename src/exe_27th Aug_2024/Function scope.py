global_p = 12

def my_function():
    a = 10
    print(a)

my_function()
print(global_p)
print(a)    #------Here a is defined under function so we cannot use it outside the function
############ Local Variable have more preference over global variable
