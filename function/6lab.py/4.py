'''Write a Python program to count the number of lines in a text file.'''

with open(r"test.txt", 'r') as file:
    x = len(file.readlines())
    print('Total lines:', x) 