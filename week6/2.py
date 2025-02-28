import re

with open("/Users/zagvozdkinaaa/PP2/week6/row.txt" , "r", encoding="utf-8") as file:
    data=file.read()

pattern= "ab{2,3}" #a is followed by 2 or 3 b
matches = re.findall(pattern, data)
print(matches)