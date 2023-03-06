'''
Write a Python program to test whether a given path exists or not. 
If the path exist find the filename and directory portion of the given path.
'''

import os
print("test whether a given path exists or not:")
path = r'C:\\Users\\Lenovo\\Desktop\\pp2\\forlab6\\a.txt'
print(os.path.exists(path))
path = r'C:\\Users\\Lenovo\\Desktop\\pp2\\forlab6\\1.txt'
print(os.path.exists(path))
print("the filename:")
print(os.path.basename(path))
print("directory:")
print(os.path.dirname(path))