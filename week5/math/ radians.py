from math import pi
def degree_to_radian(degrees):
    return degrees * (pi / 180)

degree = int(input())
print(f"{degree_to_radian(degree):.6f}")
    