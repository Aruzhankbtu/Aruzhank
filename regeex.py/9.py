"""
9. Write a Python program to insert spaces between words 
starting with capital letters.
"""
import re
s9 = str(input())

resus9 = re.findall(r'[A-Z]{1}[a-z]\w*',s9)

for i in resus9:

    print(i, '')