import math, time

def delayed_sqrt(num, miliseconds):
    time.sleep(miliseconds/1000)
    return math.sqrt(num)

number=int(input())
miliseconds=int(input())
result=delayed_sqrt(number, miliseconds)
print(f"Square root of {number} after {miliseconds} miliseconds is {result}")