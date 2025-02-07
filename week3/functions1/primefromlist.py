n=int(input())
list=[]
for i in range(n):
    num=int(input())
    list.append(num)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for el in list:
    if is_prime(el):
        print(el)