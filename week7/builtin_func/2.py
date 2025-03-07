def count_case(str):
    upper_count=sum(1 for char in str if char.isupper())
    lower_count=sum(1 for char in str if char.islower())
    return upper_count, lower_count

str=input("Enter a string: ")
upper, lower = count_case(str)
print("Uppercase: ", upper)
print("Lowercase: ", lower)