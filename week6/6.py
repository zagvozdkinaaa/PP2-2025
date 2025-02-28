import re

with open("/Users/zagvozdkinaaa/PP2/week6/row.txt" , "r", encoding="utf-8") as file:
    data=file.read()

pattern= r"[ ,.]" #replace space, comma, or dot with a colon
replaced = re.sub(pattern, ':', data)
print(replaced)