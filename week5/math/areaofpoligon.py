from math import tan, pi

def area(n, l):
    return (n * l**2) / (4 * tan(pi / n))

n=int(input())
l=int(input())
print(f"{area(n,l):.0f}")