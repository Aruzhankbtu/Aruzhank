'''
Write a Python program to convert degree to radian.
Input degree: 15
Output radian: 0.261904
'''
import math
degree = int(input())
aru = float(degree / 180)
rad = aru * 3.14285
print('%.6f' % rad)