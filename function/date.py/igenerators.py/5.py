#Implement a generator that returns all numbers from (n) down to 0
import generator
n4 = int(input())
def rev(n):
    while(n>=0):
        print(n)
        n-=1
rev(n4)