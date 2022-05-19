'''

@Author: Akshay palande

@Date: 2022-05-18 06:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2022-5-18 06:00:30

@Title : Basic Python programming

'''

"""

4. Write a Python program to print the documents (syntax, description etc.) of Python built-in
function(s).
Sample function : abs()
Expected Result : mat
abs(number) -> number
Return the absolute value of the argument.

"""

print(abs.__doc__)

# Python code to illustrate
# abs() built-in function

# floating point number
float = -54.26
print('Returned the absolute value of float is:', abs(float))

# An integer
int = -94
print('Returned the Absolute value of integer is:', abs(int))

# A complex number
complex = (3 - 4j)
print('Returned the Absolute value complex is:', abs(complex))
print()

"""

Python documentation strings (or docstrings) provide a convenient way of associating  documentation  with  Python  modules, functions, classes, and methods. An object’s docsting is defined by including a string constant as the first statement in the object’s definition

"""

#Write a Python program to print the documents (syntax, description etc.) of Python builtin function(s).

print(abs.__doc__)
print(all.__doc__)
print(any.__doc__)
print(ascii.__doc__)