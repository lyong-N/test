# print("Welcome to the  Rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the Rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     elif age >= 65:
#         print("Please pay $2.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


'''
BMI = weight (kg)/height^2(m^2)
'''

# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in m: "))
# MBI = weight/(height)**2

# if MBI < 18.5:
#     print(f"Your MBI is {round(MBI)}, you are underwight. ")
# elif MBI > 18.5 and MBI < 25:
#     print(f" Your BMI is {round(MBI)}, you have a normal weight. ")
# elif MBI > 25 and MBI < 30:
#     print(f" Your BMI is {round(MBI)}, you are slightly overweight. ")
# elif MBI > 30 and MBI < 35:
#     print(f" Your BMI is {round(MBI)}, you are obese. ")
# else:
#     print(f" Your BMI is {round(MBI)}, you are \033[1m clinically obese. \033[0m ")

'''
OR Best option
'''

# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in m: "))
# BMI = round(weight/height**2)
#
# if BMI < 18.5:
#     print(f' "Your BMI is {BMI}, you are underwight." ')
# elif BMI > 18.5:
#     print(f' "Your BMI is {BMI}, you have a normal weight." ')
# elif BMI > 25:
#     print(f' "Your BMI is {BMI}, you are slightly overweight." ')
# elif BMI > 30:
#     print(f' "Your BMI is {BMI}, you are obese." ')
# else:
#     print(f' "Your BMI is {BMI}, you are clinincally obses." ')

#print("This is bold text looks like:",'\033[1m  Python  \033[0m')

"""
***This is a Difficult Challenge********
Write a program that tells you if a year is Not Leap ot Leap year

Instructions:
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap year have 366,
with an extra day in February. The reason why we have leap years is really fascinating

This is how you work out whether a particular year is a leap year.

on every year that is evenly divisible by 4
*except* every year that is evenly divisible by 100
unless the year is also evenly divisible by 400



"""

year = int(input("Enter any year to check if its Leap or Not: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f" The year {year}, is a Leap year. ")
        else:
            print(f"The year {year}, is Not Leap year. ")
    else:
        print(f"The year {year}, is a Leap year. ")
else:
    print(f"The year {year}, is Not a Leap year. ")