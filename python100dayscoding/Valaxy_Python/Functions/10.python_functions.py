'''
===> A function is a block of code for some specific operation
===> Function code is re-usable
===> A function executes only when it is called
'''

'''
scripts to clear your terminal and list docs
'''

import os
import time
import platform

'''
if platform.system()=="windows":
    print("Please wait. Cleaning the screen.......")
    time.sleep(2) # This is sleep time for two seconds before the next action
    os.system("cls")
    print("Please wait finding the list of the directory and files")
    time.sleep(2)
    os.system("dir")
else:
    print("Please wait. Cleaning the screen.......")
    time.sleep(2) # This is sleep time for two seconds before the next action
    os.system("clear")
    print("Please wait finding the list of the directory and files")
    time.sleep(2)
    os.system("ls lrt")
'''
'''
Reduce the number of lines in your code with repeated command as above
'''
'''

def mycode(cmd1, cmd2):
    print("Please wait. Cleaning the screen.......")
    time.sleep(2) # This is sleep time for two seconds before the next action
    os.system("cmd1")
    print("Please wait finding the list of the directories and files")
    time.sleep(2)
    os.system("cmd2")

if platform.system()=="linux":
    mycode('clear', 'ls -lrt')
else:
    mycode("cls", "dir")
'''

'''
import os
import time
import platform


if platform.system()=="Windows":
    print("Please wait. Cleaning the screen.......")
    time.sleep(2)
    os.system("cls")
    print("Please wait finding the list of the directories and files")
    time.sleep(2)
    os.system("dir")
else:
    print("Please wait. Cleaning the screen.......")
    time.sleep(2)
    os.system("clear")
    print("Please wait finding the list of the directories and files")
    time.sleep(2)
    os.system("ls -lrt")
'''




'''
the above logic is repeated in two places let see how to reduce it with the same outcome
'''

def mycode(cmd1,cmd2):
    print("Please wait. Cleaning the screen.......")
    time.sleep(2)
    os.system(cmd1)
    print("Please wait finding the list of the directories and files")
    time.sleep(2)
    os.system(cmd2)

if platform.system()=="Windows":
    mycode('cls', 'dir')
else:
    mycode("clear", "ls -lrt")