"""
5. Write a Python program that matches a string that has an `'a'`
 followed by anything, ending in `'b'`.
"""
import re
s5 = str(input())

result5 = re.match(r'a\w*b',s5)

print(result5.group(0))