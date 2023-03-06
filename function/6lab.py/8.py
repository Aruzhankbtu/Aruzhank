'''
Write a Python program to delete file by specified path. 
Before deleting check for access and whether a given path exists or not.
'''

import os

path = r'C:\\Users\\Lenovo\\Desktop\\pp2\\forlab6\\b.txt'
if os.path.exists(path)==True:
    os.remove(path)
