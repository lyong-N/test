''''
Datat structures are used to store a collection of data and there are 4 types of data structures
-> List ---> []
-> Tuple --> ()
-> Dictionary --> {}
-> Set --> {}
Data structures are also known as variables
eg
x= 5
y= [1,2,2,, 'yes', ]
'''
# List s are mutable
#my_list=[] # empty list
#bool(empty_list)==>False
#my_list1=[3,2,4,"Python",5.6]
#bool(non-empty_list)==> True
#print(f"{my_list1, type(my_list1)}") # check the class of your data

''' 
print(f"{my_list1[3]}")
print(f"{my_list1[4]}")
print(f"{my_list1[-5]}")
printing particular character in your list
'''
'''
very important. let say you want to print the word "y" in Python. First you need to print python then position of y
print(f"{my_list1[3]}")  will print Python
print(f"{my_list1[3][1]}") will print y in Python
'''

'''
Three ways to print a whole list
print(f"{my_list1}")
print(f"{my_list1[:]}")
print(f"{my_list1[0:]}")

To modify a character in your list
my_list1[position of character you want to change]=new character
'''
#my_list1[0]=59
#print(f"{my_list1}")

# Manipulating Lists
#Index
my_list=[3,5,2,7,3,8,9,5,0]
#print(f"{my_list.index(5)}") # gives the position of 5. what if we had repeated numbers and you want to know their position
#print(f"{my_list.index(5,2)}") # 2 gives the second position of 5 = 7

#Count
#print(f"{my_list.count(5)}") #will print number of times 5 apears in the list

'''
Add number to your list by using append. this will add the number at the end
'''
my_list.append(100)
#print(f"{my_list}")

'''
use insert to add a number to your list at any given location of your choice
'''
my_list.insert(2,50) # 2 is the position you want to insert 50
#print(f"{my_list}")

'''
extend used to add numbers in a list to the another list
'''
my_new_list=[5,7.9,48]
my_list.extend(my_new_list)
#print(f"{my_list}")

''' 
my_list.remove(8) # this will remove the number in bracket
my_list.pop() # will remove the last letter in your list
my_list.pop(3) # will remove the character at position 3 of your list
'''
# Sort will arrange your date in acending order
my_list.sort(reverse=True) #Will sort and reverse your list
print(f"{my_list}")
# reverse will print reverse of your data
#my_list.reverse()
#print(f"{my_list}")