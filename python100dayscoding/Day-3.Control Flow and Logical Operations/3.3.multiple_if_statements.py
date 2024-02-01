'''
Logic to know


********if/elif/else**********
if condition1:
    do A
elif condition2:
    do B
else:
    do C
Here once one condition is satisfied the code stops

**** multiple if************
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C
Here all the conditions are checked

We are going to use the Rollercoaster example
'''

# print("Welcome to the  Rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the Rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age <= 65:
#         bill = 12
#         print("Adult tickets are $12.")
#     else:
#         bill = 3
#         print("Grandparent tickets are $3.")
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("Sorry, you have to grow taller before you can ride.")

'''
Instructions
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
Based on the user's oeder, work out their final bill

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for Small Pizza: +$2
Pepperoni for medium and Large Pizza: +$3

Extra cheese for any size Pizza: +$1
'''

'''
Solution
'''

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size Pizza do your want? Please select Small, Medium or Large: ")
# add_pepperoni = input("Do you want Pepperoni? Y or N: ")
# extra_cheese = input("DO you want extra cheese? Y or N:  ")
# Bill = 0
# Small = 15
# Medium = 20
# Large = 25
# if size == Small:
#     Bill = 15
#     print(f" Your Small size Pizza is $15")
# elif size == Medium:
#     Bill = 20
#     print(f"Your Medium size Pizza is $20")
# if add_pepperoni == "Y":
#     Bill += 2
# if extra_cheese == "Y":
#     Bill += 1
#     print(f" Your Total bill is ${Bill}")
# else:
#     Bill = 25
#     print(f" Your Large size Pizza is $25")


# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
# Bill = 0
# S = 15
# M = 20
# L = 25
# if size == S:
#     bill = 15
#     print(f" Your Small size Pizza is $15")
# if size == M:
#     bill = 20
#     print(f"Your Medium size Pizza is $20")
#
# if add_pepperoni == "Y":
#     Bill += 2
# if extra_cheese == "Y":
#     Bill += 1
#     print(f" Your Total bill is ${Bill}")
# else:
#     Bill = 25
#     print(f" Your Large size Pizza is $25")
#
# else:
#     print("Sorry, you have to grow taller before you can ride.")
'''
Correction
'''
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f" Your total bill is ${bill}\nThank You!")

