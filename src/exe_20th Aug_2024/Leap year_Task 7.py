#Create a program that determines whether a given year is a leap year.

#A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#Use an if-else statement to make this determination.

a = int(input("Enter the Year - "))

if (a%4==0 and a%100 != 0)or  a%400==0 :
    print(a," is a leap year")
else:
    print(a, " is not a Leap Year")