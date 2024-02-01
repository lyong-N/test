'''
getpass()
1) prompts the user for a password without echoing.
2) The getpass module provides a secure way to handle the password prompts where programs interact with  the user via
the terminal

getuser()
function displays the login name of the user. This function checks the environment variables LOGNAME, USER, LNAME, and USERNAME,
in order and returns the value of the first non-empty string
'''

#vim get_pw
import getpass
#db_pass=getpass.getpass() # default
db_pass=getpass.getpass(prompt="Enter your db pw: ")