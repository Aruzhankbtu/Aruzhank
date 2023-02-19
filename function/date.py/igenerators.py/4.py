'''
Implement a generator called squares to yield the square 
of all numbers from (a) to (b). Test it with a "for" loop and print each of 
the yielded values.
'''
import generator
r1 = int(input())
r2 = int(input())
def squares(r1, r2):
    for i in range(r1, r2):
        print(i**2)
squares(r1, r2)