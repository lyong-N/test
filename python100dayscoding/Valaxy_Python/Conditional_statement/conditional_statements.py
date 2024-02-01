'''
if is called simple conditional statement. used to control the execution of set of lines or block of code or one line
if expression:
statement1
statment2

Comparision operators
identity
membership
logical operators

the above four (4) can be used to execute the if expression
'''

#Eg read a string and
usr_str=input("Enter your string: ")
usr_cnf=input("Do you want to convert your string into lower case? Say yes or no: ")
if usr_cnf=="yes":
    print(f"{usr_str.lower()}")
else:
    print(f"{usr_str}")