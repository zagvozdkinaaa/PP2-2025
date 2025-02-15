def downto0(n):
    for i in range(n, -1, -1):
        yield i

n=int(input())
for num in downto0(n):
    print(num)