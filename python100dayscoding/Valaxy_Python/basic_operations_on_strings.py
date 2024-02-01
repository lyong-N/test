# my_name = "Lyonga"
# my_new_name = "John"
# my_job_history="""I started as a SA
# moved to Devops
# """
# print(f"my real name is: {my_name} \nMy new name is: {my_new_name} \nMy job history is: {my_job_history}")


# my_str = ""
# my_new_str = " "
# print(f'{bool(my_str)}') # Gives false because my_str is empty
# print(f'{bool(my_new_str)}') # Gives True because an empty space is counted as a character in Python

lang = "Python Scripting"
#print(f'{lang[0]}')
# print(f'{lang[0:6]}')
# j = "Lyonga Ngombe"
# print(f'{j[7:]}')  #Print only Ngombe
# print(f'{j[0:6]}') #Print only Lyonga or
# print(f'{j[:6]}')

# Length of a string use the function "len"
# z = "python tutorials"
# print(f'Length of z is: {len(z)}')

#Additing two strings together concantinate is just addition reminder space is a character in Pyhton
# a = "Python"
# b = "Scripting"
# c = a+" "+b      # best option instand of adding a space at the beginning of b or end of a
# print(c)

# n = 1234567890
# for x in str(n):
#     print(int(x)) #printing individual numbers

# h = 'Lyonga'
# for y in str(h):
#     print(str(y)) #printing individual letters

### Case conversion

# my_name = "Lyonga Ngombe Bwangai"
# print(f"{my_name}")
# print(f"{my_name.lower()}")
# print(f"{my_name.upper()}")
# print(f"{my_name.title()}")

# my_new_str="python scripting"
# print(f"{my_new_str.swapcase()}")

### Count, Index and Find operations on String

#x="python is easy and is a popular language"
#print(f"{x.count('is')}")
#print(f" Is appears {x.count('is')} in the statement")
# print(f"{x.index('p')}") #First location of p
# print(f"{x.index('p', 2)}")  # Second location of p
# print(f"{x.index('p', 25)}") # Third location of p
# print(f"{x.find('is')}")
# print(f"{x.find('easy')}")



### Join, Center and zfilll string operations

a = "python"
y = "_".join(a)
#print(f"{y}") # additing a _ between each letter
#print(f"\n".join(a)) #see the output print each letter in a line
#print(f"\n".join(y))

#print(f"\t".join(a)) # printing each letter with a space

## CENTER
# my_new ="Python Scripting"
# yes="string operations"
# print(f"{my_new.center(20)}\n{yes.center(20)}")
# #print(f"{yes.zfill(30)}")

### Practing string operations  display left center and left. By default its left
import os
t_w=os.get_terminal_size()
j=input("Enter your string: ")
# print(f"{j.center(t_w)}")
# print(f"{j.ljust(t_w}")
# print(f"{j.rjust(t_w)}")

print(j.center(t_w))
### Import os
# os.get_terminal_size()