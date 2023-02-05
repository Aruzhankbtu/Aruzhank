""" 
5.Напишите функцию, которая принимает строку от пользователя,  
и распечатайте все перестановки этой строки 
""" 
from itertools import permutations 
 
def perm(str): 
    p = permutations(str) 
    for i in p: 
        print(i) 
 
string = input() 
perm(string)