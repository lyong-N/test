'''
To read a string you must provide an input
eg user_str=input("Enter your string: ")
convert string to title format

if you have just two condition (yes and no) use if and else
'''

# user=input("Enter your string: ")
# user_confirmation=input("Do you want to convert your given string into title format? Say yes or no?:  ")
# if user_confirmation=="yes": # if this condition is true,
#     print(f"{user.title()}") # this is executed
# else:
#     print(f"{user}")

'''
if you have three outcomes eg a = b 
a can be greater than b
a can be less than b or 
a can be equals to be
In such a case we have if, elif and else
'''
a = eval(input("Enter your first number: "))
b = eval(input("Enter your second number: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else: # instant of else, you can have elif a==b
    print(f"{a} and {b} are equal")