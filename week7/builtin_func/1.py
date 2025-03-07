import math

def multiply_list(nums):
    return math.prod(nums)

n=int(input("Enter the naumber of elements: "))
nums=[]
for i in range(n):
    num=int(input("Enter an element: "))
    nums.append(num)
print("The product: ", multiply_list(nums))