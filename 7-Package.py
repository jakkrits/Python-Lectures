'''
Package in python is a folder with .py files.
It must contain __init__.py in that folder.
'''

import getpass
print(getpass.getuser())

# to avoid using dot notation, call getuser directly
from getpass import getuser
print('User: ' + getuser())

import os
current_directory = os.path.curdir
print(current_directory)
print(os.path.abspath(current_directory))

from os.path import abspath, curdir
current_directory_1 = curdir
print(current_directory_1)
print(abspath(current_directory_1))

from os import remove, rename
the_file = open("new_file.txt", "w")
the_file.close()
rename(curdir + "/new_file.txt", curdir + "/new_file_renamed.txt")
# rename here only work with unix based, use 'join' below.
remove("new_file_renamed.txt")

from os.path import join
os.makedirs("newDir")
# use first name run only, for illustration purpose.
the_file = open("./newDir/more_file.txt", "w")
the_file.close()
rename(join("newDir", "more_file.txt"), join("newDir", "renamed.txt"))
remove(join("newDir", "renamed.txt"))

from os import listdir, rmdir
print(listdir("newDir"))
rmdir("newDir")

# Excercise
# make a program to find and list abspath
# of folders in your current directory.
# use isDir in os.path
# make use of custom Exception.
from os.path import isdir, abspath, curdir
class DirectoryFound(Exception):
    pass

def detect_directories():
    for item in listdir(curdir):
        if isdir(item):
            raise DirectoryFound(abspath(item))

detect_directories()