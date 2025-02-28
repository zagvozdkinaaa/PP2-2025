import re

with open("/Users/zagvozdkinaaa/PP2/week6/row.txt" , "r", encoding="utf-8") as file:
    data=file.read()

pattern= r"\b[A-Z][a-z]+\b" #start with one uppercase and followed by lowercase
matches = re.findall(pattern, data)
print(matches)