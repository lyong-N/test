#For dectionaries we us { } an must have a key: value eg {'apply': 'fruit', 'fox': 'animal' } etc

#my_dict={'apple': 'fruit', 'fox': 'animal', 1:'one', 'two': 2}
# apply, fox, 1 and two are keys.
#print(f"{my_dict}")
# Value are stored in key. to get the value you call the key
#print(f"{my_dict['apple']}") # Prints fruit
# print(f"{my_dict.get('apple')}") # Prints fruit best option (two method to get the same answer)
#my_dict.clear() #clean you dict
#print(f"{my_dict}")
#Adding a value to a dic
# my_dict['three']=7
# print(f"{my_dict}") #if the value exits, it will be assigned the new values
# my_dict['three']= 20
# print(f"{my_dict}")

# print(f"{my_dict.keys()}") # to get your keys
# print(f"{my_dict.values()}") # To get your values
# print(f"{my_dict.items()}") #Prints key:value together

## Update your Dictionary

# new_dic={'four': 90}
# my_dict.update(new_dic)
# print(f"{my_dict.items()}")

## POP to remove a key: value from a dictionary

# my_dict.pop('apple')
# print(f"{my_dict}")
#
# ## popitem removes random numbers
#
# my_dict.popitem()
# print(f"{my_dict}")
#
# # To check removed Item
# removed_item=my_dict.popitem()
# print(f"{removed_item}")


## fromkeys is used to create a dic eg
# keys=['a', 'b', 'c']
# new_dic=dict.fromkeys(keys)
# print(f"{new_dic}")
#
# # to add a value to key
#
# new_dic['a']='first alphabet letter'
# print(f"{new_dic}")

## Setdefault Once a key is set, it can't be changed with the same number

my_dic={}
my_dic.setdefault('Lyonga', 50)
#print(my_dic)
my_dic.setdefault('Lyonga', 55) #result 50
#print(my_dic)
my_dic.setdefault('John', 50)
print(f"{my_dic}")