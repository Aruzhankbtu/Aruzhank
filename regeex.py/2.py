"""
2. Write a Python program that matches a s
tring that has an `'a'` followed by two to three `'b'`.
"""
import re
s2 = str(input())

res = re.match(r'a[b]{2,3}',s2)

print(res.group(0))