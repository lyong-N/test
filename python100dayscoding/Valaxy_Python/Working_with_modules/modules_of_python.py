'''
Modules shorten the length of your code

WHAT IS A MODULE: A module is a file containing Python definitions and statements. That means module containing
python functions, classes and variable
What is the use of module?
===> Reusability
There are two types of modules
==> Default modules
==> third party modules

USE PIP to install any third party module you need to use
eg pip install boto3
pip install paramiko (paramiko is used to work with remote server)
pip install xlwt, xlrd(read excel)



VERY IMPORTANT

Different ways to Import modules
1) Using Import math
2) using from:
    from math import * (*) means all functions in math

Difference from 1 and 2
if you use option 1 then you write
import math
print(math.pi)

if you use option 2:
from math import *
print(pi)

from math import pi (this will be the only module imported for your use)

short form to import modules
import subprocess as sp (you use sp in your script)
import platform as pt

'''

'''
How to use modules
First write your script eg mymodule.py
import the module where you need it by "import mymodule"
To see the value of the imported module, print(module name.the variable you want to print)
See example below with 
'''
# import mymodule # this is when you write yourown module
# print(mymodule.my_value)
'''
For Python pre-installed modules, import them directly. 
To know the pre-installed modules run help('modules') 

How to work with a module
import the module then 
dir(the module) 
Want to work with math module
import math
dir(math)
help(math) to get an idea of how the module works
'''

#help("modules")


import platform
print(platform.processor())