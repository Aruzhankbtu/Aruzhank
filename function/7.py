""" 
7.При наличии списка ints возвращает значение True, 
 если массив содержит 3 рядом с 3 где-то. 
 """ 
def три(a): 
    for i in range(len(a)-1): 
        if a[i]==3 and a[i+1]==3: 
            return True 
    return False 
 
a = list(map(int, input().split())) 
print(три(a))