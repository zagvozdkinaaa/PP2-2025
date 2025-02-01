heads=35
legs=94
# x+y=35
# 2x+4y=94
def solve(numheads, numlegs):
    for chickens in range(numheads+1):
        rabbits= numheads - chickens
        if 4*rabbits + 2*chickens==numlegs:
            return chickens, rabbits
    return "No solution"
print (solve(heads, legs))