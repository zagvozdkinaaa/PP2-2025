def genSquares(n):
    for i in range(1, n+1):
        yield i**2

n=int(input())
for num in genSquares(n):
    print(num)