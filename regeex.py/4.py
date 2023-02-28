"""
4. Write a Python program to find the sequences of one upper case letter
 followed by lower case letters.
"""
import re
s4 = str(input())

results4 = re.findall(r'[A-Z]{1}[a-z]\w*',s4)

print(results4)

