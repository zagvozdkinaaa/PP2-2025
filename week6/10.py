import re

with open("/Users/zagvozdkinaaa/PP2/week6/row.txt", "r", encoding="utf-8") as file:
    data=file.read()

#convert camelCase to snake_case
pattern = r'(?<!^)(?<!_)([A-ZА-Я])'
converted=re.sub(pattern, lambda match: '_' + match.group(1).lower(), data)
print(converted)