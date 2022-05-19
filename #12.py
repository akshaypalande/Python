'''

@Author: Akshay palande

@Date: 2022-05-18 9:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2022-05-18 9:00:30

@Title : Basic Python programming

'''

# 12. Write a python program to call an external command in Python.

# import os
# print(os.system('ls -l'))

import os
pipe=os.popen("dir *.md")
print (pipe.read())