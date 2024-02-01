'''
Here we will talk about Functions with Variable length keyword-based arguments
'''

def display(a, b):
    print(a)
    print(b)
    return None
display(4,5)
display(b=6,a=7)
#display(a=6, b= 7, c=8) # this will error because c is not defined
'''
To display line 11, use
'''

def me(**kwargs): # kwargs is called key argument and is a varibale so can take any value and found a dictionary
    print(kwargs)
    return None
me(a=1,b=2,c=3,d=9)

def me(p, **kwargs):
    print(p)
    print(kwargs)
    return None
me(60,a=1,b=2,c=3,d=9)
