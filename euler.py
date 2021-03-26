import math

def dxdy(x, y):
    f = 2 * y + math.exp(x) - x
    return f

a = 0.0
b = 1.0
h = 0.1
alphe = 0.25

while (b - a) > h / 2:
    z = alphe + (h * dxdy(a, alphe))
    alphe = z
    a += h
    print("f(" + str(a) + ")=" + str(z))