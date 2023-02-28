"""
6. Write a Python program to replace all occurrences of space, 
comma, or dot with a colon.
"""
import re
s6 = str(input())

ress6 = re.sub(r'[\s,.]',':',s6)

print(ress6)