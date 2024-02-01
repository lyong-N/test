## strip is used to remove space from your string. NOTE it only used to remove beginning and ending words or letter
#w="Python"
#print(f"{w}")
#print(f"{w.strip()}") # removes the space before python
#print(f"{w.strip('n')}")
#print(f"{w.split('t')}")

v="python scripting is very easy python"
#print(f"{v.strip('python')}") #Removes python at beginning and end defualt
#print(f"{v.rstrip('python')}") # notice .rstrip and it removes python at the end
#print(f"{v.lstrip('python')}") # Removes python from the left

# x="python./i"
# print(f"{x.strip('./i')}") # removes ./i
# print(f"{x.split('t')}")
#SPLIT
w="python is an easy language and is very popular"
print(f"{w.split('is')}")