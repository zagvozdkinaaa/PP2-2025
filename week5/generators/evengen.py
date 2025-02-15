def genEven(n):
    for i in range(2, n+1, 2):
            yield i

n=int(input())
print(", ".join(map(str, genEven(n))))