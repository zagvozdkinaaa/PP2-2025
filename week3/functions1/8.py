def spy_game(nums):
    for i in range(len(nums)-1):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
            return True
    return False
n=int(input())
list=[]
for i in range(n):
    num=int(input())
    list.append(num)
print(spy_game(list))
