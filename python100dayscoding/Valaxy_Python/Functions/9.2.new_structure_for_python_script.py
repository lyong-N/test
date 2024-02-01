'''
Each time you need to start a function use the format below
'''

import sys
import os
import time
import datetime

def addition(a,b):
    print(f"The addition of {a} and {b} is: {a+b}")
    return None

def main():
    x=9
    y=12
    addition(x,y)
    return None

if __name__ == '__main__':
    main()