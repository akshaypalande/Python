'''

@Author: Akshay palande

@Date: 2022-05-18 10:30:30

@Last Modified by: Akshay Palande

@Last Modified time: 2022-05-18 10:30:30

@Title : Basic Python programming

'''

#11. Write a Python program to check whether a file exists.

# importing os module 
import os
   
# Specify path
path = 'D:/CFB/Python programs/Practice programs/#11.txt'
   
# Check whether the specified
# path exists or not
isExist = os.path.exists(path)
print(isExist)
   
   
# Specify path
path = 'D:/CFB/Python programs/Practice programs/#11.py'
   
# Check whether the specified
# path exists or not
isExist = os.path.exists(path)
print(isExist)