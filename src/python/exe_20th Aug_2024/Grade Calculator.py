#Write a programm to print grade a per marks accquired by student
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#E: 50-49

a = int(input("Enter your Marks- "))

if 90 <= a <= 100:  #90 <= a >=100
    print("Grade is A")
elif 80 <= a <= 89:
    print("Grade is B")
elif a>=70 and a<=79:
    print("Grade is B")
elif a>=60 and a<=69:
    print("Grade is B")
elif a>=50 and a<=59:
    print("Grade is B")
elif 40 <= a <= 49:
    print("Grade is B")
elif a>100 and a<0:
    print("Superman")
else:
    print("Fail")



