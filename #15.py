'''

@Author: Akshay palande

@Date: 2022-05-18 11:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2022-05-18 11:00:30

@Title : Basic Python programming

'''

# 15. Write a python program to access environment variables.


import os
for item, value in os.environ.items():
   print('{}: {}'.format(item, value))