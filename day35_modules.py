# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

import math
# import math as m
# from math import e

a, b, c, d, e = 1, 2, 3, 4, 5

print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)

import example
pi = 3.1459

def square(x):
     return x ** 2

def cube(x):
     return x ** 3

def circumference(radius):
     return 2 * pi * radius

def area(radius):
     return pi * radius ** 2

result = example.pi

print(result)