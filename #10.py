'''

@Author: Akshay palande

@Date: 2022-05-18 9:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2022-05-18 9:00:30

@Title : Basic Python programming

'''

"""

10. Write a Python program to print out a set containing all the colors from color_list_1 which
are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

Expected Output :
{'Black', 'White'}

"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:\n")
print(color_list_1)
print(color_list_2)
print("\n\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))