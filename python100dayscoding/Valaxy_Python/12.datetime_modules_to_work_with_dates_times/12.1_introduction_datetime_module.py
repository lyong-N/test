'''
Datetime module is a python built-in or default module and used to work with dates and times

'''

'''
to print your current date and time in python. First import the module datetime
'''
#import datetime
# print(datetime.datetime.now()) # used to get various timezones
# print(datetime.datetime.today()) # this gives local time zone


'''
print(datetime.datetime.now()) # can be used to look for year, month, day, hour, minute, and second
'''
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)
# print(datetime.datetime.now().today())
# print(datetime.datetime.now().hour)
# print(datetime.datetime.now().minute)
# print(datetime.datetime.now().second)

'''
get only year, month and day in various format 
Check https://strftime.org/ for cheatsheat
'''
'''

print(datetime.datetime.now().strftime("%y-%m-%d")) # prints 23-05-17

print(datetime.datetime.now().strftime("%Y-%m-%d")) # prints 2023-05-17

print(datetime.datetime.now().strptime("%A")
'''
'''
Instand of writing datetime.detetime use from datetime import datetime becuse datetime is a module in datetime
'''
from datetime import datetime
print(datetime.now().strftime("%y-%m-%d")) # prints 23-05-17

print(datetime.now().strftime("%Y-%m-%d")) # prints 2023-05-17

print(datetime.now().strftime("%A")) # prints Day of the week

