'''
Follow the logic here
requirement
read a number and increase by 10
'''

'''
num=eval(input("Enter your number: "))
result=num+10
print(f"Your result is: {result}")
'''

'''
The above can written as a function
'''
def get_result():
    result=num+10
    print(f" Your result is: {result}")
    return None
num=eval(input("Enter your number: "))
get_result()