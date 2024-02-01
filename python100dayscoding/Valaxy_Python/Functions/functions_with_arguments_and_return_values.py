'''
a=eval(input("Enter your first number: "))
b=eval(input("Enter your second number: "))
result=a+b
print(f"{a} plus {b} is: {result}")
'''
'''
convert the above to functions
'''

'''
def get_addition(a,b):
    result=a+b
    print(f"{a} plus {b} is: {result}")
    return None

def main():
    a=eval(input("Enter your first number: ")) # in this form this fuct will only call a and b and not get_addition
    b=eval(input("Enter your second number: "))
    get_addition(a,b) # Now the whole function will be called
    return None

main()
'''
'''
important concert manipulate functions
'''

'''

def get_addition(a,b):
    result=a+b
    #print(f"{a} plus {b} is: {result}")
    return result

def main():
    a=eval(input("Enter your first number: "))
    b=eval(input("Enter your second number: "))
    result=get_addition(a,b)
    print(f"{a} plus {b} is: {result}")
    return None

main()

'''

'''
Another way of writing calling a function
'''

def multiple_num_10(value):
    #result=value*10 # lines 52 and 53 or just line 54 will give same result
    #return result
    return value*10

def main():
    num=eval(input("Enter your number: "))
    result=multiple_num_10(num)
    print("The result is : ", result)

main()