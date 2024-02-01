'''
Function with a fixed argument
'''

'''

def display(a):
    print(type(a))
    return None
display(1)
display("Lyonga")
display(3,4) # this throws an error because the function can only take one variable
'''


'''
variable length argument
'''


'''

def me(*data):  # * means any value
    print(data)
    return None
me() # Gives a tuple is ()
me(4) # prints (4,)
me(1,2,3,4) # prints (1, 2, 3, 4) why without a , after last number
'''
'''
prints same results are above
'''

'''

def me(*lyonga):  # after * you can write whatever you want
    print(lyonga)
    return None
me()
me(4)
me(1,2,3,4)
'''


def display(*arg):
    for item in arg:
        print(type(item))
    return None
display(4,5,6,7,8,9,10)
print('===.===.===.===.')
display("Hi Lyonga", 4.67, 6)