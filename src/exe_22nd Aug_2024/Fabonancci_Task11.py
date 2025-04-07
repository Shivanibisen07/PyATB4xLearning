#Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

# Number of terms in the Fibonacci series
n = int(input("Enter the number of terms: "))

a, b = 0, 1

print("Fibonacci series:", end=" ")

for i in range(n):
    if i == 0:
        print(a, end=" ")
    elif i == 1:
        print(b, end=" ")
    else:
        c = a + b
        print(c, end=" ")
        a, b = b, c