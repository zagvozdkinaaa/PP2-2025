import re

f = open("/Users/zagvozdkinaaa/PP2/week6/row.txt", "r", encoding="utf-8")
data = f.read()

pattern=r"\b[A-ZА-Я][^A-ZА-Я\n]*"
matches=re.findall(pattern, data) #split string at uppercase
print(matches)
