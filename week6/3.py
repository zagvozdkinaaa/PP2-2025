import re

with open("/Users/zagvozdkinaaa/PP2/week6/row.txt" , "r", encoding="utf-8") as file:
    data=file.read()

pattern= r"\b[a-z]+_[a-z]+\b" #lowercase letters joined with underscore
matches = re.findall(pattern, data)
print(matches)