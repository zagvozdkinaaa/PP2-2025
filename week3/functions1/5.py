from itertools import permutations
s=input()
def print_permutations(str):
    perm_list=permutations(str)
    for perm in perm_list:
        print(''.join(perm))
print_permutations(s)