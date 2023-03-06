'''
Write a Python program with builtin function to multiply all the numbers 
in a list
'''

import math
list1 = list(map(int, input().split()))

result1 = math.prod(list1)

print(result1)

