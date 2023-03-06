'''
Write a Python program with builtin function that accepts a string and calculate the number of 
upper case letters and lower case letters
'''

def number_of_upper_and_lower(str):
    d = dict(upper=0, lower=0)
    for i in str:
        if i.isupper():
            d["upper"] += 1 
        elif i.islower():
            d["lower"] += 1
        else:
            continue
    print ("Upper case : ", d["upper"])
    print ("Lower case : ", d["lower"])

number_of_upper_and_lower("Dict is - BuiltIn Function")