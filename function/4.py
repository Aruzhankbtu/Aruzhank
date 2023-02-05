""" 
4.Вам предоставляется список чисел, разделенных пробелами.  
Напишите функцию filter_prime которая будет принимать список чисел в качестве  
агрумента и возвращать из списка только простые числа 
""" 
 
def filter_prime(s): 
    a = [] 
    for i in s: 
        count = 0 
        for j in range(1,i+1): 
            if i%j==0 and i!=2: 
                count += 1 
        if count == 2: 
            a.append(i) 
    print(a) 
 
s = list(map(int, input().split())) 
filter_prime(s)