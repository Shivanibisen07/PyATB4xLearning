#1. No return type and No Parameter
def greet():
    print("hello")

result = greet()
print(result)

#2. No return type and with argument
def greet_by_name(name):
    print("hello,",name.upper())
greet_by_name("Shivani")

#3. No return type with default argument
def say_hello_to_default_arg(name="Arman"):
    print("Hello,",name)
say_hello_to_default_arg()
say_hello_to_default_arg("Bhavik")
say_hello_to_default_arg(name="Aamish") #----------positional argument

#multiple arguments
def multiple_arguments(name1="Arman", name2="Shivani", name3="Bisen"):
    print("Multiple Arguments",name1, name2, name3)

multiple_arguments(name1="Ram", name2="Sita", name3="Lakshman")
multiple_arguments(name1="Shivani")

#4. Argument + Return type
def sum_of_two_num(num1=60, num2=80):
    return num1+num2

#result = sum_of_two_num(num1=10, num2=20)
result = sum_of_two_num()
print(result)



