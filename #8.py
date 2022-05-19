'''

@Author: Akshay palande

@Date: 2022-05-18 7:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2022-02-18 7:00:30

@Title : Basic Python programming

'''


# 8. Write a Python program to create a histogram from a given list of integers.

def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])