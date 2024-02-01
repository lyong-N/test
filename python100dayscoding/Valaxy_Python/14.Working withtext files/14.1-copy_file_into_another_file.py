'''
How to copy a file into another file using Python or
copy the contents of a file to another file
'''

sfile="AMBA" # sfile
dfile="new1.docx" #dfile
sfo=open(sfile,'r')
content=sfo.read()
sfo.close()
dfo=open(dfile)