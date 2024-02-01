#Data Types

#Strings

# print("Hello"[0])
# print("Hello"[4])
# print("Hello"  " World!")
# print("123" + "345")



#Integer



# Boolean = True or False
#eg
# num_char = len(input("What is your name?"))
# print("Your name has " + num_char + "characters. ")
# this breaks the code b/c you can't add integer to words. To do this operation, we need to convent the int to a str

# num_char = len(input("What is your name?\n"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters. ")

# Use the type function to investigate the type of data you are working with and you can use
# functions like string, int, or float to convert to that data type

# You can change data types to meet your need in a code

# Int
b = (12345)
# print(b)
# print(type(b))

# float
# b = float(12345)
# print(type(b))


# string

b = str(12345)
print(type(b))




# eg 
# a = (1234)
# print(type(a))



#Very intresting and nice to konw

# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
#print(type(two_digit_number))
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# two_digit_number = first_digit + second_digit
# print(two_digit_number)


# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):



# Warning you should convert the result to a whole number.

# Example Input
# weight = 80
# height = 1.75
# Example Output
# 80 ÷ (1.75 x 1.75) = 26.122448979591837
# 26
# e.g. When you hit run, this is what should happen:



# Hint
# Check the data type of the inputs.
# Try to use the exponent operator in your code.
# Remember PEMDAS.
# Remember to convert your result to a whole number (int).
# Test Your Code
# Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.

# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# bmi = int(weight) / float(height) ** 2
# print(int(bmi))
#
# #f-string very important function
# score = 0
# height = 1.8
# isWinning = True
# print(f"your score is  {score}, your height is {height} and your winning is {isWinning} ")
#
# # Calculate days, months, years left on Earth
# age = input("What is your current age?\n")
# age_as_int = int(age)
# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12
#
# time_left = (f"You have {years_remaining} years, {months_remaining} months, or {weeks_remaining} weeks, or {days_remaining} days remaining on Earth if you are lucy to live up too 90 years old. ")
# print(time_left)