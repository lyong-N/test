'''
NB: When reading a number we use "eval" function
when reading a string we use "input" function
'''


# my_even_nu=[0,2,4,6,8,10,12,14,16]
# usr_num=eval(input("Enter your number: "))
#
# if usr_num in my_even_nu:
#     print(f"Number is even and in the list {my_even_nu}")
# else:
#     print(f"Number is odd and not in my list {my_even_nu}")


'''
NB: if you write "if" in your statements, python will try to run all of them even if it finds the right one
To avoid this, please use "elif" With elif once the right condition is met the run stops
'''
'''

num=eval(input("Enter any number between 1-10 range: "))
if num in [1,2,3,4,5,6,7,8,9,10]:
    if num == 1:
        print('one')
    elif num == 2:
        print('two')
    elif num == 3:
        print('three')
    elif num == 4:
        print('four')
    elif num == 5:
        print('five')
    elif num == 6:
        print('six')
    elif num == 7:
        print('seven')
    elif num == 8:
        print('eight')
    elif num == 9:
        print('nine')
    elif num == 10:
        print('ten')
else:
    print("out of range number. Please select a number between 1-10 range")
'''
'''
Another way of writing the above code using dictionary
NB: Dictionary are key === value
the below code is very neat compared to the above one but they get the same results
'''
num=eval(input("Enter any number between 1-10 range: "))
num_word={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
if num not in [1,2,3,4,5,6,7,8,9,10]:
    print(num_word.get(num))
else:
    print("out of range number. Please select a number between 1-10 range")