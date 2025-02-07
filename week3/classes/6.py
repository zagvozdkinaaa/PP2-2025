def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n%i==0:
            return False
    else:
        return True

n=int(input())
lst=[]
for i in range(n):
    num=int(input())
    lst.append(num)
primeNums=list(filter(lambda x: isPrime(x), lst))
print(primeNums)