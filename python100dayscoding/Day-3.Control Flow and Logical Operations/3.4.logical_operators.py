'''
CHeck multiple conditions in the same line of code
if condition1 and condition2 and condition3:
do this
else:
do this
'''

'''
Logical Operators 
A and B ===> both A and B must be true for whole statement to be true 

C or D ===> only one statement needs to be true 

not E

'''


print("Welcome to the  Rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the Rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <=55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")