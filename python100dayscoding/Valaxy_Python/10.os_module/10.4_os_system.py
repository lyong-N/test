'''
os.system() is used to execute os commands on your system
'''

import os # eg
# os.getcwd()
# os.system("pwd")
# os.listdir()
# os.system("ls")
# os.system("clear")

'''
**********
you can not assign a variable to os.system and it prints the results. No need to use print
**********
'''
#rt = os.system("ls") # it will list but the file. if files don't exit then it will store zero in rt
cmd="date"
os.system(cmd) # prints the time
