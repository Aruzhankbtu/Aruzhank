'''
Define a function with a generator which can iterate the numbers, 
which are divisible 
by 3 and 4, between a given range 0 and n.
'''
import generator
n3 = int(input())
c = [i for i in range(n3) if i % 3 == 0 or i % 4 == 0]
