'''
Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
'''
import math
n = int(input("Number of sides:"))
s = int(input("Length of the side:"))
area = (n * s * s) / (4 * math.tan(math.pi/n))
print(area)