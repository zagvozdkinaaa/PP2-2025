def is_palindrome(st):
    for i in range(len(st)//2):
        if st[i]!=st[len(st)-i-1]:
            return False
    return True
s=input()
print (is_palindrome(s))
