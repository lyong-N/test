'''
Search a file in your system
very powerful
'''

'''
import os
req_file=input("Enter your file name to search: ")
for r,d,f in os.walk("/"):  #For windowns for r,d,f in os.walk("c:\\")# r = root, d = directory and f = file
    for each_file in f:
        if each_file==req_file:
            print(os.path.join(r,each_file))
'''
'''
system independent script
'''

import os
import string
import platform

req_file=input("Enter your file name to search: ")

if platform.system()=="Windows":
    pd_names = string.ascii_uppercase
    vd_names = []
    for each_drive in vd_names:
        if os.path.exists(each_drive + ":\\"):
            vd_names.append(each_drive + ":\\")
        print(vd_names)
        for each_drive in vd_names:
            for r, d, f in os.walk(each_drive):
                for each_f in f:
                    if each_f == req_file:
                        print(os.path.join(r, each_f))
else:
    for r, d, f in os.walk("/"):
        for each_file in f:
            if each_file == req_file:
                print(os.path.join(r, each_file))

