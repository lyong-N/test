
"""
def display(a):
    print("The value of a is: ", a)
    return None
#dispplay() # will display an error becuase a is not defined. You need a number or string
display("Lyonga")
"""

'''

def display(a=1): # a=1 is the default argument or value.
    print("The value of a is: ", a)
    return None
display() # Will take the default values stated in your fxt
display("Lyonga")


def add_number(a,b):
    result=a+b
'''
'''
def add_numbers(a,b):
    result=a+b
    print("The result is: ", result)
    return None
add_numbers(4,5)
add_numbers(5) # gives an error becuase b is not defined
'''

"""

def add_numbers(a,b=6): # i have given b=6 a default value of 6
    result=a+b
    print("The result is: ", result)
    return None
add_numbers(5)
"""
'''

def add_numbers(a=7,b=6):
    result=a+b
    print("The result is: ", result)
    return None
add_numbers()
'''

'''
def add_numbers(a,b=8): # This will not work as the default value most be written at the end in this case b
    result=a+b
    print("The result is: ", result)
    return None
add_numbers(1)
'''
def working_on_some(user="root"):
    print(f"Working with {user}")
    return None
working_on_some() # THis will print root
working_on_some("Lyonga") #This will print "Lyonga" as i have passed it as variable