def is_palindrome(str):
    return str==str[::-1]

str=input("Enter a string: ")
if is_palindrome(str):
    print("Palindrome")
else:
    print("Not palindrome")