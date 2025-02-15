from math import fsum
def area(h, a, b):
    return fsum([a,b]) * h/2

h=float(input())
a=float(input())
b=float(input())
print(area(h,a,b))