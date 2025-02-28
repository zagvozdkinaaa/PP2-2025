import re

with open("/Users/zagvozdkinaaa/PP2/week6/row.txt", "r", encoding="utf-8") as file:
    data=file.read()

pattern=r'(?<!^)(?<!\s)([A-ZА-Я])' 
splitted=re.sub(pattern, r' \1', data) #insert space between upercase
print(splitted)
