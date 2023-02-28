"""
1. Write a Python program that matches a string that has an `'a'` 
followed by zero or more `'b'`'s.
"""
import re
s1 = str(input())

res = re.match(r'a[b]*',s1)

print(res.group(0))