





'''
def addition(a,b):
    print(f"The addition of {a} and {b} is {a+b}")
    return None

def sub(a,b):
    print(f"The sub of {a} and {b} is {a - b}")
    return None

x=7
y=4
addition(x,y)
sub(x,y)
'''


'''
refining my script1 so when its called in script2, it uses the values found in script2
'''
'''

def addition(a,b):
    print(f"The addition of {a} and {b} is {a+b}")
    return None

def sub(a,b):
    print(f"The sub of {a} and {b} is {a - b}")
    return None
def main():
    x=7
    y=4
    addition(x,y)
    sub(x,y)
    return None
#main()  # At this point if you run script2 you get the same result
if __name__ == '__main__': # with this line of code running script1 in script2 will use the values in script2
    main()
'''

'''
Understanding __name__ variable
'''
print(f"This is from script1:",__name__) # gives __main__ as output












'''

def add(a,b):
    print(f"The addition of {a} and {b} is {a+b}")
    return None
def sub(a,b):
    print(f"The sub of {a} and {b} is {a-b}")
    return None
def mult(a,b):
    print(f"The multiplication of {a} and {b} is {a*b}")
    return None
def main():
    x=7
    y=4
    add(x,y)
    sub(x,y)
    mult(x,y)
    return None
if __name__=="__main__":
    main()
'''

