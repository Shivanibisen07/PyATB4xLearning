def outer_function():
    var1 = 30

    def inner_function():
        print(var1)

    def inner2_function():
        print(var1)

    inner_function()
    inner2_function()

outer_function()