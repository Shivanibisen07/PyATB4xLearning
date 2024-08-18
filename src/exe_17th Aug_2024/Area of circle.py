#Calculate and prit area of circle using formula - area = 3.14*r^2
import math

radius=float(input("Enter the Radius of Circle- "))
area = math.pi*pow(radius,2)
#area = math.pi*(radius**radius)
print("Area of Circle is ", area)
print(f"Area of Circle is- , {area:.2f}")