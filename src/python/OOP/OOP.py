class Employee:
    def __init__(self, name, age, email, phone, address):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.address = address

    def print_info(self):
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Email   : {self.email}")
        print(f"Phone   : {self.phone}")
        print(f"Address : {self.address}")
        print("-" * 40)


def make_employee(number):
    print(f"\nLet’s enter details for Employee #{number}:")
    name = input("  Name: ")
    age = input("  Age: ")
    email = input("  Email: ")
    phone = input("  Phone: ")
    address = input("  Address: ")
    return Employee(name, age, email, phone, address)


# Build two employees
emp1 = make_employee(1)
emp2 = make_employee(2)

print("\nHere are the details you entered:\n")
print("Employee 1:")
emp1.print_info()
print("Employee 2:")
emp2.print_info()
