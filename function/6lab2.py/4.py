'''
Write a Python program that invoke square root function after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
'''

from time import sleep
import math
def delay(fn, ms, *args):
    sleep(ms / 1000)
    return fn(*args)

a = int(input())
miliseconds = int(input())
print(f"Square root of {a} after {miliseconds} is {delay(lambda x: math.sqrt(x), miliseconds, a)}")
