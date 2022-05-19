'''

@Author: Akshay palande

@Date: 2022-05-18 10:30:30

@Last Modified by: Akshay Palande

@Last Modified time: 2022-5-18 10:30:30

@Title : Basic Python programming

'''





#2 Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23') """

# List and Tuple

values = input("enter the sample data:  ")
list = values.split(", ")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


