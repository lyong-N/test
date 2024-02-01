'''
Standard for writing a function:
def xyz():
    kkkk
    kkkkk
    kjjjjj
    return None

Global variable are written outside of the fxt while
Local variable are written within the function

NB: Python will give preference to local variable than global variable when running. if there is no local variable
then it will look for global.
'''
'''
def myfunction1():
    print("welcome to functions")
    return None # Doesn't print the function To print a function you must call its name in the different line
myfunction1()               # This will print the function

def myfounction2():
    print("Thank you!")
    return None
'''

'''
TO call a different function within a function
'''
'''

def myfunction1():
    x = 40 # this is a local variable as it can only be used by fun1
    print("welcome to functions")
    print("x value from fun1: ", x)
    myfounction2()
    return None
#myfunction1() # this gives an error, it has to be after myfunction2 to read it


def myfounction2():
    print("Thank you!")
    print("x value from fun2: ", x)
    return None

def main():
    global x # without this, fuc2 will return an error. This makes x global variable although its within main() Not a good idea
    x = 10
    myfunction1()

main()
'''


# another way of calling a varibale

def myfunction1():
    x = 40 # this is a local variable as it can only be used by fun1
    print("welcome to functions")
    print("x value from fun1: ", x)
    myfounction2(x)
    return None
#myfunction1() # this gives an error, it has to be after myfunction2 to read it


def myfounction2(y): # y is called a Parameter
    print("Thank you!")
    print("x value from fun2: ",y)
    return None

def main():
    #global x
    x = 10
    myfunction1()
    myfounction2(x)  #x is called an Argument

main()