# sent = "Lyonga was playing Football"
# print(len(sent))
# print(sent[:10]) # Print Lyonga only


'''
Placeholder in string
%s stands for strings
%d stands for integers
'''

# name = "Dean"
# sentance = "%s is 20 years old"

'''
check the various out comes 
'''
# print(name)
# print(sentance)
# print(sentance % name)
# #print(name % sentance) # gives an error. The placeholder comes first followed by % before the variable
#
# name = "jake"
# sentance = "%s %s was the President of the US"
# print(sentance % ("Dean", "Lyonga"))

# a = 15
# b = 30
# print(f" The addition of 15 and 30 divided by 2 is: {(a+b)/2}")


#shopping_list = ['Apples', 'Pears', 'Mangos', 'Oranges', 'Cheese']
# print(shopping_list) # prints all
# print(shopping_list[0]) #prints Apples
# print(shopping_list[-1]) # prints Oranges
'''
add an item
'''
# shopping_list.append('lettice')
# print(shopping_list)
'''
remove an item
'''
# del shopping_list[1] # deletes item in position 2 in your list
# print(shopping_list)

'''
replace an item
'''
# shopping_list[0] = 'blueberries' #replaces item in position 0 in your list
# print(shopping_list)

'''
Finding the length,  max and min number in a list
'''

# list_number = [1,4,6,20,609,408,245,687]
# print(len(list_number))
# print(max(list_number))
# print(min(list_number))

'''
write a function that will print the records in groups of three (3)
'''
# list = {
#     'records': [1,2,3,4,5,6,7,8,997,5]
# }
#
# '''
# Solutions
# '''
# batched_list = {
#     'batched': [
#         [1,2,3],
#         [4,5,6],
#         [7,8,997],
#         [5]
#     ]
# }
#
# def records(a,b,c):
#     print(f'records in batches: {a,b,c}')
#     return None
# batched_list(a,b,c)

'''
Dictionaries {}
'''

# names = ['Dean', 'Jim', 'Peter']
# print(names[0])

'''
Conditional Statements
'''

if 3 < 2:
    print("hello")
else:
    print(f"3 is not less than 2")