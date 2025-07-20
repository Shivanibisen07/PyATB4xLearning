#Create a prog to sum of three number from user input

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

def sum_of_numbers(n1, n2, n3):
    return num1+num2+num3

result = sum_of_numbers(num1, num2, num3)
print(result)
result = sum_of_numbers(n1=num1, n2=num2, n3=num3)
print(result)