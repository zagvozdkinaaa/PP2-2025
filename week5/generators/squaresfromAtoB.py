def squares(a,b):
    for i in range(a,b+1):
        yield i**2

a=int(input())
b=int(input())
for num in squares(a,b):
    print(num)