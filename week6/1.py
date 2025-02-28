import re

with open("/Users/zagvozdkinaaa/PP2/week6/row.txt" , "r", encoding="utf-8") as file:
    data=file.read()

pattern= "ab*" #a is followed by 1 or 0 b
matches = re.findall(pattern, data)
print(matches)