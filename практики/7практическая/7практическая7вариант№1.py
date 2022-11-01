import math import*
x = float(input())
y = float(input())
z = float(input())
t = float(input())
d = sqrt(x*x+y*y) 

def a(x, y):
    return x*y*0.5 
def b(d, z, t):
    p = (z+t+d) / 
    return sqrt(p*(p-z)*(p-t)*(p-d))

print(a + b)