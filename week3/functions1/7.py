def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
n=int(input())
list=[]
for i in range(n):
    num=int(input())
    list.append(num)
print(has_33(list))