#Write a python program to get user input of their age,height and weight
#and calculate their BMI.

print("Hello!")
age=int(input("Enter your age: "))
height=float(input("Enter your height (in meter): ",))
weight=float(input("Enter your weight: "))

bmi=weight/(height*height)
print("\nYour bmi is:",bmi)
