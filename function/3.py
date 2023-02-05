""" 
3.Напишите программу для решения классической головоломки:  
Мы считаем 35 голов и 94 ноги среди кур и кроликов на ферме.  
Сколько у нас кроликов и сколько кур? создать функцию: solve(numheads, numlegs): 
""" 
def solve(numheads, numlegs): 
    chicken =  (4 * numheads - numlegs)//2 
    rabbit = (numlegs - 2 * numheads)//2 
    print(f"number of chickens = {chicken}") 
    print(f"number of rabbits = {rabbit}") 
 
heads = 35 
legs = 94 
solve(heads, legs)