'''
Write a Python program with builtin function that checks whether a passed 
string is palindrome or not.
'''
def palindrome(str):
    for i in str:
        for j in reversed(str):
            if i==j:
                return True
            return False
        

print(palindrome('ata'))
print(palindrome('almaty'))
print(palindrome('atam'))
print(palindrome('almatyytamla'))
