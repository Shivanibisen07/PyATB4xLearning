# Write a program to print max between 3 numbers

a = float(input("Enter num1-"))
b = float(input("Enter num2-"))
c = float(input("Enter num3-"))

if a > b and a > c:
    print("Greater number is ", {a})
elif b > a and b > c:
    print("Greater number is ", {b})
else:
    print(f"Greater number is ", {c})

result = max(a,b,c)
print(result)
