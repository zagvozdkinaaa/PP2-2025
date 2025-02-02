def histogram(lst):
    for num in lst:
        print('*'*num)
list=[]
n=int(input())
for i in range(n):
    num=int(input())
    list.append(num)
histogram(list)