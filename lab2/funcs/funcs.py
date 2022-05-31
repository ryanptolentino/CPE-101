import math

#square input
def square(x):
    return x*x

#f(x) = 7x^2 + 2x
def f(x):
    return x*x * 7 + 2*x

#g(x, y) = x^2 + y^2
def g(x, y):
    return (x*x) + (y*y)

#finds c in the triangle
def hypotenuse(a, b):
    return math.sqrt((a*a) + (b*b))

#checks if positive
def is_positive(x):
    return x >= 0