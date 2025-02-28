import re

with open("/Users/zagvozdkinaaa/PP2/week6/row.txt" , "r", encoding="utf-8") as file:
    data=file.read()

pattern= r"\ba.+b\b" #start with a followed by anything and ends with b
matches = re.findall(pattern, data)
print(matches)