from math import prod

def area(a, h):
    return prod([a,h])

a=float(input())
h=float(input())
print(f"{area(a,h):.1f}")