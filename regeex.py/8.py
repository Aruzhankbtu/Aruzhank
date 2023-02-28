#8. Write a Python program to split a string at uppercase letters.
import re
s8 = str(input())

resus8 = re.split(r'[A-Z]',s8)
print(resus8)