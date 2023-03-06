'''Write a Python program to write a list to a file.'''

fruits = ["apple", "orange", "kiwi"]
with open('test2.txt', "w") as myfile:
    for i in fruits:
        myfile.write(i+'\n')
        

file = open('test2.txt')
print(file.read())