#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
import generators
n2 = int(input())
b = [i for i in range(n2) if i % 2 == 0]