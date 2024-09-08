#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides,
#determine if the triangle is equilateral (all sides are equal),
#isosceles (exactly two sides are equal), or scalene (no sides are equal).
#Use an if-else statement to classify the triangle.

l1 = float(input("Enter the Length1-"))
l2 = float(input("Enter the Length2-"))
l3 = float(input("Enter the Length3-"))

if l1==l2==l3:
    print("It is an Equilateral Triangle")
elif l1==l2 or l2==l3 or l3==l1:
    print("It is an isosceles triangle")
else:
    print("It is an scalen triangle")