def solve(numheads, numlegs):
    for chickens in range(numheads+1):
        rabbits= numheads - chickens
        if 4*rabbits + 2*chickens==numlegs:
            return chickens, rabbits
    return "No solution"

if __name__ == "__main__":
    heads=35
    legs=94
    print (solve(heads, legs))