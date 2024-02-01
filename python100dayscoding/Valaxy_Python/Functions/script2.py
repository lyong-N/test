
'''
But we have a script in script1 i want to use in script2
First you have to import the script
To check what it contains run print(dir(name of script))
'''

'''

import script1
#print(dir(script1)) # this will show the functions in script1
def mult(a,b):
    print(f"The mult of {a} and {b} is {a*b}")
    return None
x=10
y=20
script1.addition(x,y) # This runs the addition and sub in script1 before addition in script2
#script1.sub(x,y)
#mult(x,y)
'''

'''
I have commented the values on script1. Hence, x= 10 and y=20 are used to execute script1
if the values in script1 are uncommented, script1 will run with values in both scripts
if x and y are commented, script1 will still run but not script2
'''
'''
I don't want the to print the values in script1 but those in script2
'''


'''
Understanding __name__ variable
'''
import script1
print(f"This is from script2:", __name__) # gives __main__ as output

'''
output of the above script is
This is from script1: script1 ===> gives script1 because I imported script1
This is from script2: __main__ ===> gives __main__

Please understand the deference above
'''














'''
import script1 # this execute script1 completely first
def div(a,b):
    print(f"The division of {a} and {b} is {a/b}")
    return None

x=10
y=20
script1.add(x,y)
script1.sub(x,y)
script1.mult(x,y)
div(x,y)
'''