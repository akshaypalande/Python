'''

@Author: Akshay palande

@Date: 2022-05-18 11:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2022-05-18 11:00:30

@Title : Basic Python programming

'''

# 14. Write a Python program to list all files in a directory in Python.

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('D:/CFB/Python programs/Practice programs') if isfile(join('D:/CFB/Python programs/Practice programs', f))]
print(files_list);
