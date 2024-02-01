'''
In Python we have two types of loops (for loop) and (while loop)

For loop is used for repeated code
for loop in python is used to iterate over a sequence (List, tuple, string) 0r other iterable objects

while loop is used to execute a block of statement repeatedly until a given condition is satisfied
'''

# j = [1,3,4,5,"yes",7,8]
# print(j)
# print(j[0])
# print(j[1])
# print(j[2])
# print(j[3])
# print(j[4])
# print(j[5])
# print(j[6])

'''
using loop for same results as above
list
'''
# for j in[3,4,5,6,"hi",9, 70,60,60,39]:
#     print(j)

'''
Tuple
'''

# for value in (4,5,6,'Hello'):
#     print("=================") # this will print 4 times as we have 4 elements in our list
#     print(value)
#     print('------------------')

'''
The above code will print ====, 4, ----- and repeat for all elements 
'''

'''
String
For string it will print number of times the letter of it eg Python will print 6 times
'''
'''
for each_char in "Python":
    print("----------", each_char) # interesting
    #print(each_char)
'''

my_list=[0,1,2,3,4,67,5,8,90,11]
for x in my_list:
    rem=x%2
    if rem==0:
        print(f"------- {x} is even number")
    else:
        print(f"--------{x} is an odd number ")



# my_string="Working with for loop"
# print(f"{my_string}")

# for j in my_string:
#     print(f"{j}") # or

#print(f"\n".join(my_string))

# my_list=[(1,2), (3,4), (5,6)]
# for j in my_list:
#     print(j) #method 1 to print values in my_list all

# my_list=[(1,2), (3,4), (5,6)]
# for f,s in my_list: # Here f represent first value and s second value.
#     print(f) # prints 1,3,5

# my_list=[(1,2), (3,4), (5,6)]
# for f,s in my_list:
#     print(s) # Prints 2,4,6

# my_list=[(1,2), (3,4), (5,6)]
# for f,s in my_list:
#     print(f,s) # prints all as method


'''
Dictionaries 
'''

my_dic={'a': 1, 'b':2, 'c':3, 'd':4}
# for each in my_dic:
#     print(each) # This only prints the key (a,b,c,d) This is bu default
# for f in my_dic.values():
#     print(f) # This will print values only

# for f in my_dic.items():
#     print(f"{f}") # This will print the key value pair

#for key,value in my_dic.items(): # VERY IMPORTANT
    #print(key)
    #print(value)
    #print(key,value)


'''
Read a directory path and identify all files and directory
you must know the path of your file
'''
# import os
# path=input("Enter your directory path: ")
# print(os.listdir(path))
