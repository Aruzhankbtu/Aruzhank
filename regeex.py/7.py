"""
7. Write a python program to convert snake case string to camel case string.
"""
import re
snake7 = str(input())

temp1 = snake7.split('_')

camel7 = temp1[0] + ''.join(i.title() for i in temp1[1:])

print(camel7) 