"""
3. Write a Python program to find sequences of lowercase letters 
joined with a underscore.
"""
s3 = str(input())

res3 = re.split('_',s3).findall(r'[a-z]\w+',s3)

print(res3)