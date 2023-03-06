"""
Python program to list only directories,
files and all directories, files in a specified path.
"""

import os
path = 'C:\\Users\\Lenovo\\Desktop\\university\\'
print("Directories:")
print([ dir_name for dir_name in os.listdir(path) if os.path.isdir(os.path.join(path, dir_name)) ])
print("Files:")
print([ file_name for file_name in os.listdir(path) if not os.path.isdir(os.path.join(path, file_name)) ])
print("All directories and files :")
print(os.listdir(path))