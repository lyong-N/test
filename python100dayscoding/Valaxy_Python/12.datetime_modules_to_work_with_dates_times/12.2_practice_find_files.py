'''
Find all the files which are older than x days
remove files older than x number of days
'''
'''

import os
import sys

req_path=input("Enter your path:  ")
age=3
if not os.path.exists(req_path):
    print("please provide valid path ")
    sys.exit(1)
if os.path.isfile(req_path):
    print("Please provide directory path ")
    sys.exit(2)
print(os.listdir(req_path))
'''

'''
The above script will list all directories and files in that path but we are interested in files only
'''

import os
import sys
from datetime import datetime
req_path=input("Enter your path:  ")
age=3 # 3 days
if not os.path.exists(req_path):
    print("please provide valid path ")
    sys.exit(1)
if os.path.isfile(req_path):
    print("Please provide directory path ")
    sys.exit(2)
today=datetime.now()
for each_file in os.listdir(req_path):
    each_file_path=os.path.join(req_path,each_file)
    if os.path.isfile(each_file_path):
        file_creation_date=datetime.fromtimestamp(os.path.getctime(each_file_path))
        #print(dir(today-file_creation_date))
        difference_days=(today-file_creation_date).days
        if difference_days > age:
            print(each_file_path,(today-file_creation_date).days)
