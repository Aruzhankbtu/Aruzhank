'''
Write a Python program to check for access to a specified path. 
Test the existence, readability, writability and executability of
 the specified path
'''

import os
print('Exist:', os.access('C:\\Users\\Lenovo\\Desktop\\university\\', os.F_OK))
print('Readable:', os.access('C:\\Users\\Lenovo\\Desktop\\university\\', os.R_OK))
print('Writable:', os.access('C:\\Users\\Lenovo\\Desktop\\university\\', os.W_OK))
print('Executable:', os.access('C:\\Users\\Lenovo\\Desktop\\university\\', os.X_OK))
