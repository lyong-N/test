'''
Identity operators are used to find the type of
===> Class
===> type
===> object
There are two types of Identity operators
===> is
===> is not
'''

'''
Membership operations very important 
use to validate the membership of a value
There are two types of membership operators
===> in
===> not in
'''
''' 

valid_java=['1.6', '1.7', '1.8', '1.9']
host_java='1.0' # change this number and observe the answer
if host_java in valid_java:
    print("host deployed with a valid java version")
else:
    print("host deployed with invalid java version")
'''


db_users=['db_admin', 'db_conf', 'db_installation']
lyonga="db_admins"  # change db_admin with groups in your list and seee the results
if lyonga in db_users:
    print('yes this user is allowed to start the db')
else:
    #print('this user is not a valid user to start db')
    print(f"this user is invalid")
