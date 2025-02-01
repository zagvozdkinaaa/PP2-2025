def unique_list(lst):
    unique_lst=[]
    for el in lst:
        if el not in unique_lst:
            unique_lst.append(el)
    return unique_lst
n=int(input())
list=[]
for i in range(n):
    num=int(input())
    list.append(num)
print(unique_list(list))