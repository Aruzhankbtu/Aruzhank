'''
Write a Python program with builtin function that returns True if all 
elements of the tuple are true.
'''

mytuple = (True, 0, False)
x = all(mytuple)
print(x) #False

mytuple2 = (1, True, True)
y = all(mytuple2)
print(y) #True