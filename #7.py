'''

@Author: Akshay palande

@Date: 2021-05-18 7:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2021-02-18 7:00:30

@Title : Basic Python programming

'''

"""

7. Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

"""


def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group_member([1, 5, 8, 3], 3))

if True:
    print("specified value is contained in a group of values")
    
print(is_group_member([1, 5, 8, 3], -1))
