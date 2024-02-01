'''
Find the java version of your hoast
'''
import os
import platform
import subprocess
cmd="java -version"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()
# print(0)
# print(f"out: {o}")
# print(f"error: {e}")
if rc==0:
    if bool(o)==True:
        print(o)
    #print(bool(o), bool(e))
    if bool(o)==False and bool(e)==True:
        print(e.splitlines()[0].split()[2].strip("\""))
else:
    print(e)


# or
'''
    if bool(o)==False:
        if bool(e)==True:
            print(e.splitlines()[0].split()[2].strip("\""))

else:
    print(e)
'''