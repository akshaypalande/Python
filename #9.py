'''

@Author: Akshay palande

@Date: 2022-05-18 9:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2022-05-18 9:00:30

@Title : Basic Python programming

'''
# 9. Write a Python program to concatenate all elements in a list into a string and return it.

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([2,5,6,85]))
