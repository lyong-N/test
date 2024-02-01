'''
This module is used to work/interact with operating system to automate many more tasks like creating directory,
removing directory, identifying current directory and many more
we will look into
os
os.path
os.system()
os.walk()

****
to get your current working directory with python run: os.getcwd()
*****

directory name is a string hence use ' ' or " "
'''
import os
print(os.sep) # to get \
print(os.getcwd()) # to get your current directory
#os.chdir("/home") # here you must provide the directory you want to move into
#print(os.chdir("/usr"))
os.listdir()
print(os.listdir(path))
os.mkdir(path) # here you can create only one directory a time
os.makedirs(path) # You can create multiple directories at a time  #recursive directory creation function
os.removedirs(path)
os.removedirs(path)#removes directories recursively
os.rmdir(path)
os.rename(src,dst) #src =source , dst= distination
os.environ
os.getgid() #group id
os.getuid() #user id
os.getpid()
