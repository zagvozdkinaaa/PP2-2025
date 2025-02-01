import math
def sphere_volume(radius):
    vol=(4/3)*math.pi*(radius**3)
    return vol
r=int(input())
print(sphere_volume(r))