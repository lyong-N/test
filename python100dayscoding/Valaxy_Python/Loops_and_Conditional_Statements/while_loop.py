'''
The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
We generally use this loop when we don't know beforehand, the number of times to iterate
'''


#for j in range(5):
    #print(f"Welcome to python loops") # prints message 5 times
    #print(f"{j}") # prints 0-4
    #print(f"{5}") # prints 5 five times

# count = 1
# while count <=5:
#     print("Hello Lyonga")
#     count=count+1 # Without this condition, this will print forever

# value=40
# while value<=79081:
#     print(value)
#     value=value+500 # what happens here is first value is 40, then 500 will be added to 40 till we get 79081

'''
Loop Control Statements: break, continue, Pass
Break is used to stop your loop
We have for loop and while loop
'''

# for each in [3,4,56,7,8,9,10]:
#     break
#     print(f"{each}"

import sys
#print("before exit")
#sys.exit() # this stops the loop
#print("after exit")
# for each in [3,4,56,7,8,9,10]:
#     break
#     print(each)
# print("after loop")


'''
the code bellow will print each number in your list and after loop
'''
# for each in [3,4,56,7,8,9,10]:
#     print(each)
# print("after loop")

'''
but what if I want to print only 3 and after loop
'''
# for each in [3,4,56,7,8,9,10]:
#     print(each)
#     break
# print("after loop")

'''
what if i want to print 3 , 4 , 56 and break
'''

# for each in [3,4,56,7,8,9,10]:
#     print(each)
#     if each ==56:
#         break
# print("after loop")

'''

'''

# paths=['/usr/bin', '/usr/bin/httpd', '/home/users/xyz/weblogic/config.xml']
# for each_path in paths:
#     if 'httpd' in each_path:
#         print(each_path)
#         break # this stops the loop once the item is found
# print("Lyonga is learning Python")


# count=1
# while True:
#     print(count) # from line 79 to 81 will print forever
#     if count == 100:
#         break
#     count = count+1 # without this line Count will not break


'''
continue
'''

# for j in range(1,11):
#     if j !=7: # prints without 7
#         print(j)

'''
or
'''
# for j in range(1,11):
#     if j ==7:
#         continue
#         print("Lyonga is doing well studying Python") # This line won't print or any other with same indentation as contiue
#     print(j) # see the indentation of print same as if


if True:
    pass # no error recorded
