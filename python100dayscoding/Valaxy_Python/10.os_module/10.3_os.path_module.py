'''
This is a sub module of OSis used to work on paths
'''

import os
# os.path.sep # sep = separator
# print(os.path.sep)
# path="/home/ec2-user/test.py"
# print(os.path.basename(path)) # This will print test.py and is called basename
# print(os.path.dirname(path)) # this will print /home/ec2-user
#os.path.join(path1,path2) # used to join paths
# path1 = "/home"
# path2 = "ec2-user"
# print(os.path.join(path1,path2))

#os.path.split(path) # Is used to split the path name into a pair head and tail eg path="/home/ec2-user/test.py"
# path="/home/ec2-user/test.py"
# print(os.path.split(path)) # result ('/home/ec2-user', 'test.py')
# path="/home/ec2-user/test.py/lyongatxt"
# print(os.path.split(path)) # result ('/home/ec2-user/test.py', 'lyongatxt') it can only split into 2

# os.path.getsize(path) #in bytes
# os.path.exists(path) # to check if a path exist before running an update sample code

# path="/home/ec2-user/test.py"
# if os.path.exists(path):
#     print("your files is there")
# else:
#     print(f"{path} is not present on this host")
'''
os.path.isfile() , os.path.isdir(path), os.path.islink(path)
After time module we will also discuss: getatime, getctime and getmtime
'''

path="/home/ec2-user/test.py"
if os.path.isfile(path):
    print(f"{path} is a file")
else:
    print(f"{path} is a directory")



