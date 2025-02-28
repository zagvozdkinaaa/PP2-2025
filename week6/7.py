import re

with open("/Users/zagvozdkinaaa/PP2/week6/row.txt" , "r", encoding="utf-8") as file:
    data=file.read()

pattern= r"_[a-zA-Z]"
converted = re.sub(pattern, lambda match: match.group(1).upper(), data) #convert snake_case to camelCase
print(converted)