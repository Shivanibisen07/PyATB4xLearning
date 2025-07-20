#Take input and create a class in python

class Person:

    def __init__(self):
        self.name = input("Enter the name\n")
        self.age = input("Enter the age\n")
        self.phone = input("Enter the phone\n")
        self.occupation = input("Enter the Occupation\n")


    def print_details(self):
        print(f"Name is {self.name}")
        print(f"Name is {self.age}")
        print(f"Name is {self.phone}")
        print(f"Name is {self.occupation}")

person1 = Person()

person1.print_details()

