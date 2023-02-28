#Write a Python program to convert a given camel case string to snake case.
import re
snake7 = str(input())

temp1 = snake7.split(' ')

camel7 ='_'.join(i.title() for i in temp1)

print(camel7)

